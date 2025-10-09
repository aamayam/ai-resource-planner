from src.nodes.initial_node import initial_node
from src.nodes.plan_generation import plan_generation
from src.nodes.self_validation import self_validation
from src.nodes.hitl_review import HITL_review
from src.nodes.routing_nodes import route_after_validation, route_after_hitl
from src.utils.graph_state import GraphState
from langgraph.graph import StateGraph, END

graph = StateGraph(GraphState)

graph.add_node("START", initial_node)
graph.add_node("plan_generation", plan_generation)
graph.add_node("self_validation", self_validation)
graph.add_node("HITL_review", HITL_review)

graph.add_edge("START","plan_generation")
graph.add_edge("plan_generation","self_validation")

graph.add_conditional_edges(
    "self_validation",
    route_after_validation,
    {
        "plan_generation": "plan_generation",
        "HITL_review": "HITL_review"
    }
)

graph.add_conditional_edges(
    "HITL_review",
    route_after_hitl,
    {
        "plan_generation": "plan_generation",
        "__END__": END
    }
)