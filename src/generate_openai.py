from openai import OpenAI

from src.prompt import get_instructions_prompt_intermediate_sentence

# Point to the local server
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def get_embedding(text, model="nomic-ai/nomic-embed-text-v1.5-GGUF"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def make_completion(message):
    history = [
        {"role": "user", "content": get_instructions_prompt_intermediate_sentence() + f"### {message} ###"}
    ]
    # new_message = {"role": "user", "content": f"### {message} ###"}
    # history.append(new_message)

    completion = client.chat.completions.create(
        model="gemma2:9b",
        messages=history,
        temperature=0.7,
        stream=True
    )
    final_response = get_all_chunks(completion)
    return final_response

def get_all_chunks(completion):
    final_response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            final_response += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="", flush=True)
    return final_response
