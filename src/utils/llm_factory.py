from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from typing import Optional
from dotenv import load_dotenv
from config.logger import setup_logger

load_dotenv()
logger = setup_logger("LLMFactory")

def create_openai_chat(model: str, temperature: float) -> ChatOpenAI: 
    if 0.0 <= temperature <= 2.0:
        try:
            llm = ChatOpenAI(model=model, temperature=temperature)
            logger.info("Open AI LLM object granted")
            return llm
        except Exception as e:
            logger.error(f"Unexpected error while creating OpenAI instance: {e}")
            raise e
    else:
        raise TypeError("Temperature must be a float between 0.0 and 2.0")
    
def create_anthropic_chat(
        model: str, 
        temperature: float, 
        max_tokens: Optional[int] = 10000) -> ChatAnthropic:
    if 0.0 <= temperature <= 1.0:
        try:
            llm = ChatAnthropic(
                model_name=model, 
                temperature=temperature,
                max_tokens = max_tokens)
            logger.info("Anthropic's Claude LLM object granted")
            return llm
        except Exception as e:
            logger.error(f"Unexpected error while generating Anthropic object: {e}")
            raise e
    else:
        raise TypeError("Temperature must be a float between 0.0 and 1.0")
