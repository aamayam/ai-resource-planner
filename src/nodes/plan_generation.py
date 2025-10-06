from src.utils.graph_state import GraphState
from src.utils.plan_structure import PlanStructure
from src.utils.llm_factory import create_anthropic_chat, create_openai_chat
from config.logger import setup_logger
from config.prompt_loader import get_model, get_temperature, get_prompt
from pydantic import BaseModel, Field
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.types import Interrupt


# client="anthropic" for Claude
MODEL = get_model(agent="generator", client="openai")
TEMP = get_temperature(agent="generator")

logger = setup_logger("PLAN GENERATION AGENT")

def plan_generation_agent(state: GraphState) -> GraphState:
    project_info = state['project_info']
    
    try:
        # substitute for create_anthropic_chat for Claude 
        GenerationLLM = create_openai_chat(model=MODEL, temperature=TEMP)
        logger.info("LLM Object succesfully created")
        StructuredLLM = GenerationLLM.with_structured_output(PlanStructure)
        logger.info("Structured output included for LLM based on PlanStructure")

        system_prompt = get_prompt(agent_name="generator", prompt_type="system")
        user_prompt = get_prompt(agent_name="generator", prompt_type="user", **project_info)

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ]
        logger.info("Calling LLM...")
        response = StructuredLLM.invoke(messages)
        logger.info("Succesfully retrieved plan from LLM")
        return {
            **state,
            "plan_info": response
        }
    except Exception as e:
        logger.error(f"Unexpected error while generating plan: {e}")
        raise ValueError("Errors occure during Generation Agent execution")
