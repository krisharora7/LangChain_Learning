from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
load_dotenv()
model = HuggingFaceEndpointEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2'
)
vector_store = Chroma(
    embedding_function=model,
    persist_directory='chroma_db',
    collection_name='sample'
)
retriever = vector_store.as_retriever(
    search_kwargs={'k':2}
)
query='India ka captain kon h?'
result = retriever.invoke(query)
print(result)