from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from langchain_classic.vectorstores import FAISS
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
load_dotenv()
llm = ChatGroq(model='openai/gpt-oss-20b')
embed_model = HuggingFaceEndpointEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2'
)
docs = [
    Document(page_content='The grand canyon is a famous natural site. ' \
    'photosynthesis is how plants convert light into energy,' \
    'many tourists visit it every year'),
    Document(page_content='Ai is booming nowadays,' \
    'Chlorophyll captures sunligh for photosynthesis.' \
    'no one knows if ai ballon will explode or not'),
    Document(page_content='Krish is currently learning langchain with CampusX Playlist daily')
]
vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embed_model
)
query = 'what is photosynthesis?'
base_retriever = vector_store.as_retriever(search_kwargs={'k':2})
compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)
result = compression_retriever.invoke(query)
for i,doc in enumerate(result):
    print(f"result no.-> {i+1} \n")
    print(f"content-> \n {doc}\n")