"""
Script que implementa um chat interativo com histórico de conversas usando o modelo Llama.
Este script cria uma interface de chat onde o usuário pode interagir com o modelo de linguagem Llama,
mantendo o histórico completo da conversa para contextualização das respostas.
Funcionalidades:
  - Interface de chat via linha de comando
  - Streaming das respostas em tempo real
  - Histórico de mensagens mantido para contexto
  - Integração com o modelo Llama através da API Ollama
Dependências:
  - ollama: Para interação com o modelo de linguagem
  - models: Módulo local contendo configuração do modelo llama31
Uso:
  Execute o script e digite suas mensagens quando solicitado.
  Para sair, use Ctrl+C.
Formato das mensagens:
  As mensagens são armazenadas como dicionários com:
    - role: 'user' ou 'assistant'
    - content: conteúdo da mensagem
"""
from ollama import chat
from models import llama31
messages = [
  {
    'role': 'user',
    'content': '',
  },
  {
    'role': 'assistant',
    'content': '',
  },
]

while True:
  user_input = input('Chat with history: ')
  
  
  response = chat(
    llama31,
    messages=messages
    + [
      {'role': 'user', 'content': user_input},
    ],
    stream=True
  )

  part_message = {
    'role': 'assistant',
    'content': '',
  }
  for part in response:
    print(part['message']['content'], end='',
          flush=True)

    # Add the response to the messages to maintain the history
    part_message['role'] =  'assistant' 
    part_message['content'] = part['message']['content']

  # Add the response to the messages to maintain the history
  messages += [
    {'role': 'user', 'content': user_input},
    {'role': 'assistant', 'content': part_message['content']},
  ]
  print('\n')  