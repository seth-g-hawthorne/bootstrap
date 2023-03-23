import openai
import os
import sys

openai.api_key = os.getenv("OPENAPI_API_KEY")
if not openai.api_key: 
    print("**** Error: Environment variable not defined: OPENAPI_API_KEY")
    sys.exit(-1)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "Why should DevOps engineer learn kubernetes?"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)