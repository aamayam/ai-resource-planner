from src.utils.graph_state import GraphState
from config.logger import setup_logger
from typing import Literal

logger = setup_logger("ROUTER")

def route_after_validation(state: GraphState) -> Literal["plan_generation","HITL_review"]:
    validation_result = state.get('validation_result')
    retry_count = state.get('retry_count')
    if validation_result.is_valid:
        logger.info("Waiting for human review...")
        return "HITL_review"
    elif not validation_result.is_valid and retry_count >= 2:
        logger.warning("Bypassed to HITL review since max retry attempts has been reached")
        return "HITL_review"
    else:
        logger.info("Routing back to Plan Generation Agent")
        return "plan_generation"
    
def route_after_hitl(state: GraphState) -> Literal["plan_generation","__END__"]:
    human_feedback = state.get('human_feedback')

    if not human_feedback.requires_rework:
        return "plan_generation"
    else:
        return "__END__"