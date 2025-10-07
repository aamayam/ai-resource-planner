from src.utils.graph_state import GraphState
from src.utils.plan_structure import PlanStructure
from src.tools.llm_factory import create_anthropic_chat, create_openai_chat
from config.logger import setup_logger
from config.prompt_loader import get_model, get_temperature, get_prompt
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.types import Interrupt


# client="anthropic" for Claude
MODEL = get_model(agent="generator", client="openai")
TEMP = get_temperature(agent="generator")

logger = setup_logger("PLAN GENERATION AGENT")

def plan_generation(state: GraphState) -> GraphState:
    project_info = state['project_info'].model_dump_json(indent=2)
    validation_result = state.get('validation_result')
    retry_count = state.get('retry_count')
    human_feedback = state.get('human_feedback')

    # If User provides feedback or comments we refactor with 'human_feedback' prompt
    if human_feedback:
        issues_text = "\n".join(f"- {issue}" for issue in human_feedback.parsed_comments)
        prompt_vars = {
            'project_info_json': project_info,
            'plan_info_json': state['plan_info'].model_dump_json(),
            'issues_list': issues_text
        }

        user_prompt = get_prompt(agent_name="generator", prompt_type="human_feedback", **prompt_vars)
    # If self validation returns the state, we use now 'retry_user' prompt to fix issues.
    elif validation_result and not validation_result.is_valid:
        # we are on a retry attempt
        issues_text = "\n".join([f"- {issue}" for issue in validation_result.issues])
        prompt_vars = {
            'project_info_json': project_info,
            'plan_info_json': state['plan_info'].model_dump_json(),
            'retry_count': retry_count,
            'issues_list': issues_text
        }
        user_prompt = get_prompt(agent_name="generator", prompt_type="retry_user", **prompt_vars)
        retry_count += 1
    else:
        # First execution on workflow. i.e. no 'validation_result' yet.
        user_prompt = get_prompt(agent_name="generator", prompt_type="user", **project_info)
    try:
        # substitute for create_anthropic_chat for Claude 
        GenerationLLM = create_openai_chat(model=MODEL, temperature=TEMP)
        logger.info("LLM Object succesfully created")
        StructuredLLM = GenerationLLM.with_structured_output(PlanStructure)
        logger.info("Structured output included for LLM based on PlanStructure")
        system_prompt = get_prompt(agent_name="generator", prompt_type="system")

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        logger.info("Calling LLM...")
        response = StructuredLLM.invoke(messages)
        logger.info("Succesfully retrieved plan from LLM")

        # TODO: include summarize tool for update summary field.
        return {
            **state,
            "plan_info": response,
            "retry_count": retry_count
        }
    except Exception as e:
        logger.error(f"Unexpected error while generating plan: {e}")
        raise ValueError("Errors occure during Generation Agent execution")
