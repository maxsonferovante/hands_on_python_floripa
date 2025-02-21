from ollama import chat
from models import llama31


messages = [{
    'role': 'user',
    'content': 'Me fala um pouco sobre a linguagem de programação Python'
}]


for part in chat(model=llama31, messages=messages, stream=True):
    print(part['message']['content'], end='', flush=True)