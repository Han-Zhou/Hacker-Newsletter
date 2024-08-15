import os
from dotenv import load_dotenv
from openai import OpenAI
from llamaapi import LlamaAPI


def create_summary(link):
    load_dotenv()
    client = OpenAI(
    api_key = os.getenv("LLAMA_API_TOKEN"),
    base_url = "https://api.llama-api.com"
    )

    response = client.chat.completions.create(
        model="llama-13b-chat",
        messages=[
            {"role": "system", "content": "You're a skilled researcher in tech, and is able to consisely summarize anything"},
            {"role": "user", "content": f"Summarize the contents of this: {link}, if unable, print out 'unrecognizable content'."}
        ]
    )
    return response.choices[0].message.content

#print(response)
# print(response.model_dump_json(indent=2))
# print(response.choices[0].message.content)