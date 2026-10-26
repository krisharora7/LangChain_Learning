from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = OpenAIEmbeddings(model='abcd', dimensions=120)
result1 = embeddings.embed_query("hi i am krish")
documents = ["hi i am krish", " how are you?", "nice to meet you"]
result2 = embeddings.embed_documents(documents)
print(str(result2))