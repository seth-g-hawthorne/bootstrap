import openai
import os
import sys

openai.api_key = os.getenv("OPENAPI_API_KEY")
if not openai.api_key: 
    print("Environment variable not defined: OPENAPI_API_KEY")
    sys.exit(-1)

url = sys.argv[1] if len(sys.argv) == 2 else 'https://www.imdb.com/list/ls053501318/'

print(f"{+ 78 * '_'}\nChatGPT-3 URL Analysis for: {url}\n{+ 78 * '_'}" )
def ask(prompt):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a chatbot"},
                {"role": "user", "content": prompt},
            ]
    )

print("Description:")
response = ask("Describe this URL: " + url)
print(''.join(choice.message.content for choice  in response.choices))

print("\nTags:")
response = ask("Generate tags for this URL: " + url)
print(''.join(choice.message.content for choice  in response.choices))


