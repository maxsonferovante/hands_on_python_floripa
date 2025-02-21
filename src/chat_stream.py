"""
Um script para interagir com a API de chat Ollama usando respostas em streaming.

Este script demonstra como usar a API de chat Ollama para gerar respostas em streaming
sobre a linguagem de programação Python. Ele usa o modelo llama31 para processar a consulta
e exibe a resposta incrementalmente.

Dependências:
    - ollama: Para integração com a API de chat
    - models: Módulo personalizado contendo definições de modelo (llama31)

O script faz o seguinte:
1. Configura um array de mensagens com uma consulta do usuário sobre Python
2. Faz streaming da resposta do modelo usando a função chat()
3. Imprime a resposta incrementalmente no console

Nota:
    O parâmetro stream=True permite o streaming em tempo real da resposta,
    proporcionando uma experiência mais interativa.
"""
from ollama import chat
from models import llama31

messages = [{
    'role': 'user',
    'content': 'Me fala um pouco sobre a linguagem de programação Python'
}]


for part in chat(model=llama31, messages=messages, stream=True):
    print(part['message']['content'], end='', flush=True)