from src.utils.questions import questions
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()
ChatLLM = ChatOpenAI(model="gpt-4o", temperature=0)

project_info = {
    'duration': None,
    'object_distribution': True,
    'onshore-offshore_split': "30:70",
    'working_hours': 160,
    'participation': True,
    'headcount': "No fixed headcount",
    'buffer': "No Buffer",
    'dependencies': "No dependencies",
    'pto-vacations': "Do not include"
}

print("Welcome! I'm the resource planner agent and I'm here to help.")
print("Please answer the next questions so I can get to know your project")
for key, item in questions.items():
    print(f"Agent: {item['question']}")
    while True:
        user_input = input("User: ")
        try:
            structured_llm = ChatLLM.with_structured_output(item['response_type'])
            messages = [
                SystemMessage(content=item['system_prompt']),
                HumanMessage(content=user_input)
            ]
            response = structured_llm.invoke(messages)

            if response.flag == 'valid':
                if "confirmation" in response.model_dump():
                    project_info[key] = response.confirmation
                elif "value" in response.model_dump():
                    project_info[key] = response.value
                else:
                    raise TypeError("Unrecognized Response Type")
                
                break
            else:
                print("Agent: please give a valid response to the question")
        except Exception as e:
            print(f"error: {e}")
            break

print(f"\n\ncurrent configuration: {project_info}")