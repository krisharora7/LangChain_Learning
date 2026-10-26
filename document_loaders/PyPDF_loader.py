from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('Krish_Research_Proposal.pdf')
docs = loader.load()
print(docs[1])
print(docs[0].metadata)
print(len(docs))