# import necessary modules.
import google.generativeai as genai
import json
import base64
import pathlib
import pprint
import requests
import mimetypes
from IPython.display import Markdown

# Configure the client library by providing your API key.
genai.configure(api_key='AIzaSyBS')

model = 'gemini-1.5-pro-latest' # @param {isTemplate: true}
contents_b64 = 'W10=' # @param {isTemplate: true}
generation_config_b64 = 'eyJ0ZW1wZXJhdHVyZSI6MSwidG9wX3AiOjAuOTUsInRvcF9rIjowLCJtYXhfb3V0cHV0X3Rva2VucyI6ODE5Miwic3RvcF9zZXF1ZW5jZXMiOltdfQ==' # @param {isTemplate: true}
safety_settings_b64 = 'W3siY2F0ZWdvcnkiOiJIQVJNX0NBVEVHT1JZX0hBUkFTU01FTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfSEFURV9TUEVFQ0giLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfU0VYVUFMTFlfRVhQTElDSVQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn0seyJjYXRlZ29yeSI6IkhBUk1fQ0FURUdPUllfREFOR0VST1VTX0NPTlRFTlQiLCJ0aHJlc2hvbGQiOiJCTE9DS19NRURJVU1fQU5EX0FCT1ZFIn1d' # @param {isTemplate: true}
user_input_b64 = '' # @param {isTemplate: true}

contents = json.loads(base64.b64decode(contents_b64))
generation_config = json.loads(base64.b64decode(generation_config_b64))
safety_settings = json.loads(base64.b64decode(safety_settings_b64))
user_input = base64.b64decode(user_input_b64).decode()
stream = False

# Call the model and print the response.
gemini = genai.GenerativeModel(model_name=model)

chat = gemini.start_chat(history=contents)

response = chat.send_message(
    user_input,
    stream=stream)

display(Markdown(response.text))

###

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

prompt = input('qual a pergunta: ')

while prompt != 'fim':
    convo.send_message(prompt)
    print(convo.last.text)
    prompt = input('qual a pergunta: ')
