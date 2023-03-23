# Launchpad: apis/openapi/chatgpt-gradio
A gradio based interface to chatGPT, derived from: [Build your chatGPT using Python](https://medium.com/@mesudhir/build-your-chatgpt-using-python-6acc77c9168)

# Pre-requisits
  1. `pip install virtualenv`
  1. Get an openap API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
  1. `export OPENAPI_API_KEY=`_your api key_


# Usage
  * Run the following commands: 
    ```
    virtualenv venv
    pip -r requirements.txt
    python3 gradio-client.py
    ```

  * Browse to: [http://127.0.0.1:7860/](http://127.0.0.1:7860/)