from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
splitter = CharacterTextSplitter(
    chunk_size = 20,
    chunk_overlap = 5,
    separator=''
)
loader = PyPDFLoader('Krish_Research_Proposal.pdf')
docs = loader.load()
text = ' hi, i am krish and i am learning langchain through campusX playlist and its 8 september today'
result1 = splitter.split_text(text)
result2 = splitter.split_documents(docs)
print(result2[0])