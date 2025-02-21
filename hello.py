import asyncio
from ollama import AsyncClient
from models import llama31

async def main():
  
    messages = [{
            "role": "user",
            "content": "Me fala um pouco sobre a linguagem de programação Python",        
        }]

    client = AsyncClient()
    
    response = await client.chat(model=llama31, messages=messages)
    
    print(response.message.content)

if __name__ == "__main__":
    asyncio.run(main())    
