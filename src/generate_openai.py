from typing import List, Optional
from openai import OpenAI
import instructor
from pydantic import BaseModel
from llmlingua import PromptCompressor

from src.prompt import get_instructions_prompt_intermediate_sentence

# Output structure for our sentences
class SentenceInfo(BaseModel):
    numero_processo: Optional[str]
    tipo_crime: Optional[str]
    pena_base: Optional[str]
    agravantes: List[str]
    atenuantes: List[str]

# Point to the local server
client = instructor.from_openai(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"),
        mode=instructor.Mode.JSON,
    )

def make_completion(message):
    history = [
        {"role": "system", "content": get_instructions_prompt_intermediate_sentence() }
    ]

    llm_lingua = PromptCompressor("microsoft/phi-2")
    compressed_prompt = llm_lingua.compress_prompt(message, target_context=8192, use_llmlingua2=True)
    new_message = {"role": "user", "content": f"\n### {compressed_prompt} ###"}
    history.append(new_message)
    
    sentenceInfo, completion = client.chat.create_with_completion(
        model="gemma:9b",
        messages=history,
        response_model=SentenceInfo
    )
    final_response = sentenceInfo.__str__()
    print(completion.choices[0].message.content)
    return final_response

