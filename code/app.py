from flask import Flask, render_template, request 
import openai  
import os
from flask import session  

app = Flask(__name__)  
  
# Configure OpenAI API credentials  
openai.api_type = "azure"
openai.api_base = "https://pmopenai.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
api_key = os.getenv("API_KEY")
if api_key is None:  
    print("Environment variable not found")  
else:  
    print(f"Environment variable value: {api_key}")  
openai.api_key = api_key  
@app.route('/')  
def home():  
    return render_template('index.html')  
  
@app.route('/chat', methods=['POST'])  
def chat():  
    print("request",request.json)
    data = request.json  
    chat_history = data['chat_history']  
    engine = data['engine']  
    temperature = data['temperature']  
    max_tokens = data['max_tokens']  
    top_p = data['top_p']  
    frequency_penalty = data['frequency_penalty']  
    presence_penalty = data['presence_penalty']  
    response = openai.ChatCompletion.create(  
        engine=engine,  
        messages=chat_history,
        temperature=temperature,  
        max_tokens=max_tokens,  
        top_p=top_p,  
        frequency_penalty=frequency_penalty,  
        presence_penalty=presence_penalty,  
        stop=None  
    )  
    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']
  
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=8000)   
