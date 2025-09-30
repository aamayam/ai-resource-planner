from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

def create_openai_chat(model: str, temperature: float) -> ChatOpenAI: 
    if 0.0 <= temperature <= 2.0:
        try:
            llm = ChatOpenAI(model=model, temperature=temperature)
            return llm
        except Exception as e:
            raise e
    else:
        raise TypeError("Temperature must be a float between 0.0 and 2.0")