from utils.graph_state import GraphState
from pydantic import BaseModel, Field

class PhaseDistribution(BaseModel):
    phase: str = Field(
        description="Phase name: Analysis, Desgin, Development, Unit Testing, SIT/UAT, Release, Hypercare")
    duration: str = Field(description="Durantion of the phase in sprints, for instance: '2 sprints'")
    effort_percentage: int = Field(
        ge=0,
        le=100,
        description="percentage of total effort covered in this phase")
    total_hours: int = Field(
        ge=0,
        description="total effor hour for this phase: should match total_effort*effort_percentage/100")

class PlanStructure(BaseModel):
    pass

def plan_generation_agent(state: GraphState) -> GraphState:
    pass