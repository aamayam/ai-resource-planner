from .response_formats import * 

questions = {
    "duration": {
        "question": "What is the confirmed duration of the project (in months)?",
        "response_type": DurationResponse,
        "system_prompt": """Extract answer to: "What is the confirmed duration of the project (in months)?"
            - flag='valid': User clearly answers yes or no
            - flag='invalid': Answer is unrelated, unclear, or doesn't address the question
            - duration: an integer indicating the number of months for the duration of the project
            """
    },
    "object_distribution": {
        "question": "Do you expect equal object distribution across all 3 releases?",
        "response_type": ObjectDistributionResponse,
        "system_prompt": """Extract answer to: "Do you expect equal object distribution across all 3 releases?"
            - flag='valid': User clearly answers yes or no
            - flag='invalid': Answer is unrelated, unclear, or doesn't address the question
            - confirmation=true: User accepts equal distribution
            - confirmation=false: User rejects equal distribution"""
    },
    "onshore-offshore_split": {
        "question": "Is the 30:70 Onshore-Offshore split acceptable? If not, please suggest a ratio.",
        "response_type": OffshoreSplitResponse,
        "system_prompt": """Extract answer to: "Is the 30:70 Onshore-Offshore split acceptable? If not, please suggest a ratio."
            - flag='valid': User clearly answers yes or no
            - flag='invalid': Answer is unrelated, unclear, or doesn't address the question
            - confirmation=true: User accepts equal distribution
            - confirmation=false: User rejects equal distribution"""
    },
    "working_hours": {
        "question": "Are the assumed working hours per month (160 hrs) accurate for your team?",
        "response_type": WorkingHoursResponse,
        "system_prompt": """Extract answer to: "Are the assumed working hours per month (160 hrs) accurate for your team? "
            - flag='valid': User clearly answers yes or no
            - flag='invalid': Answer is unrelated, unclear, or doesn't address the question
            - confirmation=true: User accepts default hours
            - confirmation=false: User rejects default hours
            - alternative_value= int with the number of working hours the user consider for their project
            """
    },
    "participation": {
        "question": "Do all roles (Associate to Director) participate equally across all releases?",
        "response_type": TeamParticipationResponse,
        "system_prompt": """Extract answer to: "Do all roles (Associate to Director) participate equally across all releases?"
            - flag='valid': User clearly answers yes or no
            - flag='invalid': Answer is unrelated, unclear, or doesn't address the question
            - confirmation=true: User accepts equal distribution
            - confirmation=false: User rejects equal distribution
            """
    },
    "headcount": {
        "question": "Do you have fixed headcount constraints for any role or region (onshore/offshore)?",
        "response_type": HeadcountResponse,
        "system_prompt": """Extract answer to: "Do you have fixed headcount constraints for any role or region (onshore/offshore)? "
            - flag='valid': User clearly answers yes or no
            - flag='invalid': Answer is unrelated, unclear, or doesn't address the question
            - confirmation=true: User has fixed headcount
            - confirmation=false: User does not have a fixed headcount
            """
    },
    "buffer": {
        "question": "Should additional buffer (e.g., 10-15%) be added for testing/rework?",
        "response_type": AdditionalBufferResponse,
        "system_prompt": """Extract answer to: "Should additional buffer (e.g., 10-15%) be added for testing/rework?"
            - flag='valid': User clearly answers yes or no
            - flag='invalid': Answer is unrelated, unclear, or doesn't address the question
            - confirmation=true: User wants to include additional buffer
            - confirmation=false: User does not want to include additional buffer
            """
    },
    "dependencies": {
        "question": "Are there parallel project dependencies that could impact available capacity?",
        "response_type": ProjectDependenciesResponse,
        "system_prompt": """Extract answer to: "Are there parallel project dependencies that could impact available capacity?"
            - flag='valid': User clearly answers yes or no
            - flag='invalid': Answer is unrelated, unclear, or doesn't address the question
            - confirmation=true: User indicates that the project have dependencies
            - confirmation=false: User indicates that the project doesn't have dependencies
            """
    },
    "pto-vacations": {
        "question": "Should we account for holidays or planned PTOs within the 3-month timeline?",
        "response_type": PTOResponse,
        "system_prompt": """Extract answer to: "Are there parallel project dependencies that could impact available capacity?"
            - flag='valid': User clearly answers yes or no
            - flag='invalid': Answer is unrelated, unclear, or doesn't address the question
            - confirmation=true: User indicates that PTO should be considered
            - confirmation=false: User indicates that PTO shouldn't be considered
            """
    }
}