from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv
from langchain_core.documents import Document
load_dotenv()

docs = [
    Document(
        page_content="""
        All-rounders are cricketers who can contribute significantly with both
        the bat and the ball. They provide balance to a cricket team.
        """,
        metadata={"topic": "cricket", "id": 1}
    ),

    Document(
        page_content="""
        Hardik Pandya is a versatile cricketer who contributes as both a
        batsman and a bowler. His ability to perform multiple roles makes him
        valuable to the team.
        """,
        metadata={"topic": "cricket", "id": 2}
    ),

    Document(
        page_content="""
        A good cricket team needs players with different skills. Some players
        specialize in batting, while others focus on bowling or fielding.
        """,
        metadata={"topic": "cricket", "id": 3}
    ),

    Document(
        page_content="""
        Software engineers need a balance of technical and problem-solving
        skills. Strong programmers can take different roles within a development
        team.
        """,
        metadata={"topic": "software", "id": 4}
    ),

    Document(
        page_content="""
        A machine learning engineer works with data, algorithms, and models.
        Good performance depends on choosing appropriate features and training
        techniques.
        """,
        metadata={"topic": "machine-learning", "id": 5}
    ),

    Document(
        page_content="""
        Team sports require players to understand their individual roles.
        Good communication and coordination can improve overall performance.
        """,
        metadata={"topic": "sports", "id": 6}
    ),

    Document(
        page_content="""
        A balanced diet provides proteins, carbohydrates, fats, vitamins, and
        minerals. Different nutrients play different roles in maintaining good
        physical performance.
        """,
        metadata={"topic": "fitness", "id": 7}
    ),

    Document(
        page_content="""
        Leadership requires a person to manage different responsibilities.
        Effective leaders balance technical knowledge, communication skills,
        and team management.
        """,
        metadata={"topic": "leadership", "id": 8}
    ),

    Document(
        page_content="""
        Cloud computing allows engineering teams to deploy applications at
        scale. Performance depends on infrastructure, networking, and resource
        management.
        """,
        metadata={"topic": "cloud", "id": 9}
    ),

    Document(
        page_content="""
        Football midfielders often perform multiple roles during a match.
        They contribute to both attack and defense while maintaining team
        balance.
        """,
        metadata={"topic": "football", "id": 10}
    )
]

llm = ChatGroq(model='openai/gpt-oss-20b')
embed_model = HuggingFaceEndpointEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2'
)
vector_store=FAISS.from_documents(documents=docs, embedding=embed_model)
retriever = vector_store.as_retriever(search_kwargs={'k':3})
advanced_retriever=MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm,
)
query = "Which people are useful because they can handle responsibilities beyond their primary specialization?"
print(f'Normal Search -> \n')
result1 = retriever.invoke(query)
for i,doc in enumerate(result1):
    print(f"result no. -> {i+1}\n")
    print(f"content -> \n {doc} \n")
print("\n\n")

print(f'Multi Query Search -> \n')
result2 = advanced_retriever.invoke(query)
for i,doc in enumerate(result2):
    print(f"result no. -> {i+1}\n")
    print(f"content -> \n {doc} \n")