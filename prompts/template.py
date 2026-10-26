from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    template='''
    You are a {profession} , help me to understand {topic}.
    explain in {tone} tone''',
    input_variables=["profession", "topic", "tone"],
    validate_template=True

)
template.save('template.json')