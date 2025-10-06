import yaml
from pathlib import Path

def load_prompts(path: str = "config/prompts/prompts.yml") -> dict:
    with open(path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)
    
PROMPTS = load_prompts()

def get_prompt(agent_name: str, prompt_type: str = 'user', **kwargs) -> str:
    template = PROMPTS['agents'][agent_name][prompt_type]
    return template.format(**kwargs) 

def get_model(agent: str, client: str = "openai") -> str:
    return PROMPTS['agents'][agent]['metadata']['models'][client]

def get_temperature(agent: str) -> float:
    return PROMPTS['agents'][agent]['metadata']['temperature']