from langchain_community.retrievers import WikipediaRetriever
retriever = WikipediaRetriever(
    top_k_results=2,
    lang='en'
)

#query
query = "AI era"

docs = retriever.invoke(query)
for i,doc in enumerate(docs):
    print(f"result no.- {i+1} \n")
    print(f"Content - \n {doc.page_content}")
# print(docs)