from src.utils.graph_state import GraphState
from config.logger import setup_logger
from typing import Literal

logger = setup_logger("ROUTER")

def route_after_validation(state: GraphState) -> Literal["plan_generation","feedback_hitl"]:
    validation_result = state.get('validation_result')
    retry_count = state.get('retry_count')
    if validation_result.is_valid:
        logger.info("Waiting for human review...")
        return "feedback_hitl"
    elif not validation_result.is_valid and retry_count >= 2:
        logger.warning("Bypassed to HITL review since max retry attempts has been reached")
        return "feedback_hitl"
    else:
        logger.info("Routing back to Plan Generation Agent")
        return "plan_generation"