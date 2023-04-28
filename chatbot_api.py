import requests
import json

API_KEY = "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"
API_URL = "https://api.openai.com/v1/chat/completions"

print("Enter 'q' or 'quit' to quit the chat\n")

def get_chatbot_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "messages":[{'role': 'user', 'content': prompt}],
        "model": "gpt-3.5-turbo",        
        
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response_json = json.loads(response.content)

    return response_json["choices"][0]['message']['content']

                

while True:
    prompt = input("\nYou: ")
    if prompt == 'q' or prompt == 'quit':
        break
    response = get_chatbot_response(prompt)
    print("Chatbot:", response)
