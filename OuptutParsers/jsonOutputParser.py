from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(
    model='openai/gpt-oss-20b',
)
parser = JsonOutputParser()
template = PromptTemplate.from_template(
    'give me name, age and city of a Avenger person \n {format_instruction}',
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
# prompt = template.format()
# result = model.invoke(prompt)
# print(result)
chain = template | model | parser
final_result = chain.invoke({})
print(f"final result: {final_result}")
