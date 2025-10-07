from pydantic import BaseModel, Field
from typing import List

class PhaseDistribution(BaseModel):
    phase: str = Field(
        description="Phase name: Analysis, Desgin, Development, Unit Testing, SIT/UAT, Release, Hypercare")
    duration: str = Field(description="Durantion of the phase in sprints, for instance: '2 sprints'")
    effort_percentage: int = Field(
        ge=0,
        le=100,
        description="percentage of total effort covered in this phase")
    total_hours: int = Field(description="Total hours for this phase, should match effort * total_effort")

class SprintAllocation(BaseModel):
    sprint: int = Field("Sprint number, secuencial from 1 to n where n is the last sprint number")
    phase: str = Field(description="phase name")
    developer: int = Field(ge=0, description="headcount for this role on this sprint")
    qa: int = Field(ge=0, description="headcount for this role on this sprint")
    tech_lead: int = Field(ge=0, description="headcount for this role on this sprint")
    ba: int = Field(ge=0, description="headcount for this role on this sprint")
    pm: int = Field(ge=0, description="headcount for this role on this sprint")
    pmo: int = Field(ge=0, description="headcount for this role on this sprint")
    leadership: int = Field(ge=0, description="headcount for this role on this sprint")

class TeamAllocation(BaseModel):
    team: str  = Field(description="Onshore/Offshore")
    developer: int = Field(ge=0, description="headcount for this role on this phase/location")
    qa: int = Field(ge=0, description="headcount for this role on this phase/location")
    tech_lead: int = Field(ge=0, description="headcount for this role on this phase/location")
    ba: int = Field(ge=0, description="headcount for this role on this phase/location")
    pm: int = Field(ge=0, description="headcount for this role on this phase/location")
    pmo: int = Field(ge=0, description="headcount for this role on this phase/location")
    leadership: int = Field(ge=0, description="headcount for this role on this phase/location")

class PhaseTeamComposition(BaseModel):
    phase: str = Field(description="Phase name")
    teams: List[TeamAllocation] = Field(
        description="List of teams (onshore/offshore) for this phase"
    )

class GeographicDistribution(BaseModel):
    role: str = Field(description="The role among the ones used on project")
    onshore: int = Field(description="Number of total hours for this role on Onshore team")
    offshore: int = Field(description="Number of total hours for this role on offshore team")
    total: int = Field(description="Number of total hours for this role resulting on adding up" \
    "onshore and offshore hours")

class ReleaseStructure(BaseModel):
    release_number: int 
    phase_distribution: List[PhaseDistribution]
    sprint_allocation: List[SprintAllocation]
    team_composition: List[PhaseTeamComposition]
    geographic_distribution: List[GeographicDistribution]

class PlanStructure(BaseModel):
    releases: List[ReleaseStructure] = Field(
        description="The actual table information for each release")
    reasoning: str = Field(description="All the explanation of what was created and assumptions made")

class ValidationOutput(BaseModel):
    is_valid: bool = Field(description="boolean indicating if the plan passes all validations")
    issues: List[str] = Field(description="list of specific issues found (empty list if valid)")