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