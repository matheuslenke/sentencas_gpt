import ollama

from src.prompt import get_instructions_prompt_intermediate_sentence

def generate_completion(prompt):
    """
    Generates a text completion using Ollama, streaming the output and returning the result.

    Args:
        prompt: The user's input prompt.
        system_prompt: (Optional) An initial system-level message to guide the generation.

    Returns:
        The complete generated text.
    """
    
    messages = []
    messages.append({"role": "system", "content": get_instructions_prompt_intermediate_sentence()})
    messages.append({"role": "user", "content": prompt})

    generator = ollama.chat(
        model="gemma2:9b-instruct-q8_0",
        messages=messages,
        stream=True,
        options={
            "temperature": 0.7,
        }
    )
    
    full_response = ""
    for chunk in generator:
        content = chunk["message"]["content"]
        full_response += content
        print(content, end="", flush=True)  # Stream to output

    return full_response