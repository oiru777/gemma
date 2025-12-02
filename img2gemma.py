from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': '画像を200文字以内で説明して',
    'images': ['./image.png']
    
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)