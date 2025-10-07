from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, List
from operator import add
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from src.utils.plan_structure import PlanStructure, ValidationOutput

# TODO: Refactor ProjectStructure to have a more accurate input
class ProjectStructure(BaseModel):
    duration: int | None = Field(default=None, description="Project duration in months")
    total_effort: int = Field(description="total estimated effort for the project")
    num_releases: int = Field(description="number of releases for this project")
    object_distribution: str = Field(
        default="Equal distribution across releases", 
        description="Object distribution across releases")
    onshore_offshore_split: str = Field(
        default="30:70",
        description="Onshore/Offshore split for the team")
    working_hours = int = Field(
        default=160,
        description="Number of working hour per month")
    participation: str = Field(
        default="Equal participation",
        description="Participation of each role across releases")
    headcount: str = Field(
        default="Fixed Headcount",
        description="Headcount constraints for any role or region")
    buffer: float = Field(
        default=0.0,
        description="Additional buffer for testing or rework")
    dependencies: str = Field(
        default="No dependencies",
        description="Parallel project dependencies that could impact available capacity")
    pto_holidays: str = Field(
        default="No PTO or holidays taken in account",
        description="Indicate if PTO or holidays should be taken into account")

class HumanFeedback(BaseModel):
    requires_rework: bool = Field(description="Boolean value indicating if graph needs to " \
    "route back to Generation Node or go to END")
    raw_comments: str = Field(description="Feedback or required changes provided by user")
    parsed_comments: List[str] = Field(description="List of required changes for the agent")
    
class GraphState(TypedDict):
    project_id: int
    project_info: ProjectStructure | None = None
    plan_info: PlanStructure | None = None
    validation_result: ValidationOutput | None = None
    retry_count: int = 0
    human_feedback: HumanFeedback | None = None
    summary: str 
    messages: Annotated[list[BaseMessage], add]