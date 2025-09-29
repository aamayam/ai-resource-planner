from pydantic import BaseModel, Field

class DurationValues(BaseModel):
    duration: int | None = Field(description="project duration in months")

class DurationResponse(BaseModel):
    flag: str = Field(description="'valid' or 'invalid' according to the user input")
    value: DurationValues

class ObjectDistributionResponse(BaseModel):
    flag: str = Field(description="'valid' or 'invalid' according to the user input")
    confirmation: bool = Field(default=True, description="'true' for accepting the equal distribution, 'false' otherwise")

class OffshoreSplitResponse(BaseModel):
    flag: str = Field(description="'valid' or 'invalid' according to the user input")
    confirmation: bool = Field(default=True, description="'true' for accepting the onshore/offshore distribution, 'false' otherwise")

class WorkingHoursResponse(BaseModel):
    flag: str = Field(description="'valid' or 'invalid' according to the user input")
    modification: bool = Field(default=True, description="'true' for accepting the default hours, 'false' otherwise")
    value: int = Field(default=160, description="Value for working hour per month")

class TeamParticipationResponse(BaseModel):
    flag: str = Field(description="'valid' or 'invalid' according to the user input")
    confirmation: bool = Field(default=True, description="'true' for accept equal participation, 'false' otherwise")

class HeadcountResponse(BaseModel):
    flag: str = Field(description="'valid' or 'invalid' according to the user input")
    confirmation: bool = Field(default=False, description="'true' for new headcount, 'false' otherwise")

class AdditionalBufferResponse(BaseModel):
    flag: str = Field(description="'valid' or 'invalid' according to the user input")
    confirmation: bool = Field(default=False, description="'true' for additional, 'false' otherwise")

class ProjectDependenciesResponse(BaseModel):
    flag: str = Field(description="'valid' or 'invalid' according to the user input")
    confirmation: bool = Field(default=False, description="'true' if there are dependencies, 'false' otherwise")

class PTOResponse(BaseModel):
    flag: str = Field(description="'valid' or 'invalid' according to the user input")
    confirmation: bool = Field(default=False, description="'true' if there are dependencies, 'false' otherwise")