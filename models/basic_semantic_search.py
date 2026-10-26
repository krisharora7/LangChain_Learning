from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
docs = [
    "virat kohli is an aggressive cricketer",
    "MS dhoni is calm cricketer",
    "Ronaldo is once most paid athlete"
]
user_query = "who is virat kohli?"
embeddings = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)
docs_vector = embeddings.embed_documents(docs)
user_vector = embeddings.embed_query(user_query)

scores = cosine_similarity([user_vector],docs_vector)[0]
index,score = sorted(enumerate(scores),key=lambda x:x[1])[-1]
print(user_query)
print(f"index of most similiar senetnce is {index}, /n senetence is {docs[index]}, /n similarity score is {score}")