import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_chat_completion(prompt):
    response = openai.ChatCompletion.create(
        model="DALL-E 3",  # Specify the correct model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000  # Adjust token limit as needed
    )
    return response['choices'][0]['message']['content'].strip()


prompt = f"Please generate an image"
response = generate_chat_completion(prompt)
print(response)