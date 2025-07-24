import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.images.generate(
    model="dall-e-3",
    prompt="an inspirational quote about hard work",
    size="1024x1024",
    quality="standard",
    n=1
)

print(response.data[0].url)
