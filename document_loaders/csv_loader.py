from langchain_community.document_loaders import csv_loader
loader = csv_loader('file.csv')
docs = loader.load()
# each row is a document means 200 rows becomes a list of 200 document objects