import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

from src.prompt import get_instructions_prompt

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

def generate(message, prompt=get_instructions_prompt()):
    '''
        This function generates content using the Gemini model.
        message: The message from user input
        prompt: the prompt to be used
    '''
    vertexai.init(project="gemini-code-project", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-pro",
        system_instruction=[prompt]
    )
    new_message = f"### {message} ###"
    responses = model.generate_content(
        new_message,
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )
    return responses[0].text

