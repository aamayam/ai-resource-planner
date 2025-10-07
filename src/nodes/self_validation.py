from src.utils.graph_state import GraphState
from src.utils.plan_structure import PlanStructure, ValidationOutput
from src.tools.llm_factory import create_openai_chat, create_anthropic_chat
from config.logger import setup_logger
from config.prompt_loader import get_model, get_temperature, get_prompt
from langchain_core.messages import SystemMessage, HumanMessage

MODEL = get_model(agent="validator")
TEMP = get_temperature(agent="validator")

logger = setup_logger("SELF VALIDATION AGENT")

def self_validation(state: GraphState) -> GraphState:
    project_info = state['project_info']
    total_effort = project_info.total_effort
    num_releases = project_info.num_releases
    plan_info = state["plan_info"].model_dump_json(indent=2)

    prompt_vars = {
        "total_effort": total_effort,
        "num_releases": num_releases,
        "plan_info": plan_info
    }

    try:
        ValidatorLLM = create_openai_chat(model=MODEL, temperature=TEMP)
        logger.info("LLM Object succesfully created")
        StructuredLLM = ValidatorLLM.with_structured_output(ValidationOutput)
        logger.info("Structured output included for LLM based on ValidationOutpur")

        system_prompt = get_prompt(agent_name="validator", prompt_type="system")
        user_prompt = get_prompt(agent_name="validator", prompt_type="user", **prompt_vars)

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        logger.info("Calling LLM...")
        response: ValidationOutput = StructuredLLM.invoke(messages)
        logger.info("Succesfully retrieved analysis from LLM")
        if not response.is_valid:
            logger.warning("Some issues have been found in the generated plan. Re-thinking now...")
        else:
            logger.info("The generated plan has been approved by self validator agent")

        return {
            **state,
            'validation_result': response,
            'human_feedback': None
        }
    except Exception as e:
        logger.error(f"Unexpected error while generating plan: {e}")
        raise ValueError("Errors occure during Generation Agent execution")

