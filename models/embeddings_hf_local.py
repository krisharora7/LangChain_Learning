from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)
documents = ["hello", " hi i am krish", " how are you?"]
result = embeddings.embed_documents(documents)
print(str(result))