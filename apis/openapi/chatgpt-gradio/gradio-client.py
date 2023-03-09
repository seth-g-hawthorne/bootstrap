# Gradio based ChatGPT client adapted from https://medium.com/@mesudhir/build-your-chatgpt-using-python-6acc77c9168 by Sudhir Adhikari
import gradio as gr 
import openai
import os
import sys

# Get key from command-line or environment variable 
if len(sys.argv) == 2:
    openai.api_key=sys.argv[1]
else:
    openai.api_key = os.getenv("OPENAPI_API_KEY")
if not openai.api_key:
    print("Usage: " + sys.argv[0] + " " + "<openapi-key>")
    exit()

# Parameters
# Temperature - controls the randomness of the generated text. Higher value more varied/creative. 
PARAM_TEMPERATURE = 0.9
# max_tokens - maximum number of tokens for the response 
PARAM_MAX_TOKENS = 150
# top_p - likelihood of generating more common responses. Higher value more common
PARAM_TOP_P=1
# frequency_penalty - controls the likelihood of generating less common responses. Higher value less common responses
PARAM_FREQUENCY_PENALTY = 0
# presence_penalty -  likelihood of generating responses that contain specific words or phrases. A higher value more likely to contain these words
PARAM_PRESENCE_PENALTY = 0.6

start_sequence = "\AI:"
restart_sequence = "\Human:"

prompt = "The following is a conversation with an AI assistant: "

def openai_create(prompt):
    response = openai.Completion.create(
           model = "text-davinci-003",
           prompt = prompt,
           temperature = PARAM_TEMPERATURE,
           max_tokens = PARAM_MAX_TOKENS, 
           top_p = PARAM_TOP_P,
           frequency_penalty = PARAM_FREQUENCY_PENALTY, 
           presence_penalty= PARAM_PRESENCE_PENALTY, 
           stop=[" Human:", " AI:"]
       ) 
    return response.choices[0].text

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history 

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>chatGPT Client</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
    
block.launch(debug = True)