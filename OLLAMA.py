'''Models Running locally'''


''' CHAT MODEL '''
from langchain_ollama import ChatOllama
model = ChatOllama(model='llama3.2:3b', temperature=1)
result = model.invoke("hi, how are you?")

#print(result)

''' LLM '''

from langchain_ollama import OllamaLLM
model2 = OllamaLLM(model='llama3.2:3b', temperature=1)
result2 = model2.invoke("capital of india")
print(result2)

''' Embeddings '''
from langchain_ollama import OllamaEmbeddings
model3 = OllamaEmbeddings(model='<model_name>')
result3 = model3.embed_query('....')