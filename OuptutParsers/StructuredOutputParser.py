from langchain_groq import ChatGroq
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)
schema = [
    ResponseSchema(name='fact 1', description = 'fact 1 of topic'),
    ResponseSchema(name='fact 2', description = 'fact 2 of topic'),
    ResponseSchema(name='fact 3', description = 'fact 3 of topic')
]
parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate.from_template(
    "generate 3 facts on the {topic} \n {format_instruction}",
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain = template | model | parser
result = chain.invoke({'topic':'social distraction'})
print(result)