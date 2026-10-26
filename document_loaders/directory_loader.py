from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader=DirectoryLoader(
    path='folder',
    glob='**/*.pdf',
    loader_cls=PyPDFLoader
)
docs = loader.load()
print(len(docs))
print(docs[5].metadata)