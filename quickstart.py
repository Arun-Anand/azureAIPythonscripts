import os
import requests
import json
import openai

#openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_key = "952d8d0aa3a24018aac112902963ea5a"
#openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_base="https://azure-openai-a1test.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

#deployment_name='REPLACE_WITH_YOUR_DEPLOYMENT_NAME' #This will correspond to the custom name you chose for your deployment when you deployed a model. 
deployment_name="openaimsaruntest"

# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Write a tagline for an ice cream shop. Ans '
response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=10)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(start_phrase+text)