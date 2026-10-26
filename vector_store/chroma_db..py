from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document
load_dotenv()
doc1 = Document(
    page_content='Virat Kohli is a batsman and indian captain who has an aggresive personality',
    metadata={'team':'RCB'}
)
doc2 = Document(
    page_content='MSD is a batsman and former indian captain who has a calm leadership',
    metadata={'team':'CSK'}
)
doc3 = Document(
    page_content='Jasprit Bumrah is a Fast Bowler and one of the best in world',
    metadata={'team':'MI'}
)
doc4 = Document(
    page_content='Ravindra Jadeja is an all rounder and know for its multi skill and good fielding',
    metadata={'team':'CSK'}
)
doc5 = Document(
    page_content='Rohit Sharma is a batsman and indian captain who is know for hitting sixes',
    metadata={'team':'MI'}
)

docs = [doc1,doc2,doc3,doc4,doc5]
model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction"
)

vector_store = Chroma(
    embedding_function=model,
    persist_directory='chroma_db',
    collection_name='sample2'
)
print(vector_store.add_documents(docs))

print('\n')
#read document
print(vector_store.get(include=['embeddings',"documents",'metadatas']))
print('\n')

#similarity score
print("search document: ",vector_store.similarity_search(query='who has high temper?',k=2))
print('\n')

#search with similarity score(distance, less is better)
print("search document with score: ",vector_store.similarity_search_with_score(query='who has high temper?',k=2))
print('\n')

#meta data filtering
print("meta data filtering: ",vector_store.similarity_search_with_score(query='',filter={'team':'MI'}))
print('\n')

#update doc
# upadted_doc = Document(
#     page_content='Virat Kohli now is retired from t20 and play only test matches',
#     metadata={'team':'RCB'}
# )
# print("Update existing document")
# vector_store.update_document(document_id='49bdabd6-c5e8-4c0a-92ee-d9c978520cac',document=upadted_doc)
# print("after update: ",vector_store.get(include=['embeddings','metadatas','documents']))
# print('\n')

# # delete doc
# vector_store.delete(ids='49bdabd6-c5e8-4c0a-92ee-d9c978520cac')
# print("after delete: ",vector_store.get(include=['embeddings','metadatas','documents']))

