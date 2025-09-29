from response_formats import * 

questions = {
    "duration": {
        "question": "What is the confirmed duration of the project (in months)?",
        "response_type": DurationResponse
    },
    "object_distribution": {
        "question": "Do you expect equal object distribution across all 3 releases?",
        "response_type": ObjectDistributionResponse
    },
    "onshore-offshore_split": {
        "question": "Is the 30:70 Onshore-Offshore split acceptable? If not, please suggest a ratio.",
        "response_type": OffshoreSplitResponse
    },
    "working_hours": {
        "question": "Are the assumed working hours per month (160 hrs) accurate for your team?",
        "response_type": WorkingHoursResponse
    },
    "participation": {
        "question": "Do all roles (Associate to Director) participate equally across all releases?",
        "response_type": TeamParticipationResponse
    },
    "headcount": {
        "question": "Do you have fixed headcount constraints for any role or region (onshore/offshore)?",
        "response_type": HeadcountResponse
    },
    "buffer": {
        "question": "Should additional buffer (e.g., 10-15%) be added for testing/rework?",
        "response_type": AdditionalBufferResponse
    },
    "dependencies": {
        "question": "Are there parallel project dependencies that could impact available capacity?",
        "response_type": ProjectDependenciesResponse
    },
    "pto-vacations": {
        "question": "Should we account for holidays or planned PTOs within the 3-month timeline?",
        "response_type": PTOResponse
    }
}