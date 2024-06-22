from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def get_embedding(text, model="nomic-ai/nomic-embed-text-v1.5-GGUF"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

async def make_completion(history, message):
    new_message = {"role": "user", "content": f"### {message} ###"}
    history.append(new_message)


    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=history,
        temperature=0.7,
        stream=True,
    )

    with open("results/result.md", "a") as result_file:
        for chunk in completion:
            if chunk.choices[0].delta.content:
                result_file.write(chunk.choices[0].delta.content)
                print(chunk.choices[0].delta.content, end="", flush=True)
        result_file.write("\n")
