from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, List
from operator import add
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI

class ProjectStructure(BaseModel):
    duration: int | None = Field(default=None, description="Project duration in months")
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
    
class GraphState(TypedDict):
    project_id: int
    llm: ChatOpenAI
    project_info: ProjectStructure
    plan_info: None
    summary: str 
    messages: Annotated[list[BaseMessage], add]