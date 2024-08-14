import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from llamaapi import LlamaAPI

load_dotenv()

# print(os.getenv("LLAMA_API_TOKEN"))

client = OpenAI(
api_key = os.getenv("LLAMA_API_TOKEN"),
base_url = "https://api.llama-api.com"
)

link = "https://comment.org/repair-and-remain/"
response = client.chat.completions.create(
    model="llama-13b-chat",
    messages=[
        {"role": "system", "content": "You're a skilled researcher in tech, and is able to consisely summarize anything"},
        {"role": "user", "content": f"Summarize this article: {link}. Keep it under 50 words."}
    ]

)

#print(response)
print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)