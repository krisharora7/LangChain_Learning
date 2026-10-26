from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document
load_dotenv()
model = HuggingFaceEndpointEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2'
)
docs = [
    Document(page_content='Langchain is a Framework'),
    Document(page_content='Langchain is a Library'),
    Document(page_content='Core components of Langchain are model, prompts and chains'),
    Document(page_content='runnables are import part of langchain'),
    Document(page_content='Embeddings are numerical vectors')
]
vector_store=Chroma.from_documents(
    documents=docs,
    embedding=model,
    persist_directory='chroma_db',
    collection_name='sample3'
)
retriever = vector_store.as_retriever(
    search_type='mmr',
    search_kwargs={'k':3, "lambda_mult":0.45}
)
query = "Tell me about Langchain"
result = retriever.invoke(query)
for i,doc in enumerate(result):
    print(f"result no.-> {i+1} \n")
    print(f"content-> \n {doc}\n")