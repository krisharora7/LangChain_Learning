from langchain_core.tools import tool , InjectedToolArg
from langchain_groq import ChatGroq
from typing import Annotated
import requests
from langchain.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()



@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """this fetches the conversion factor from an API"""
    url = f'https://v6.exchangerate-api.com/v6/514855134641c7266ee02a82/pair/{base_currency}/{target_currency}'
    response = requests.get(url)
    return response.json()['conversion_rate']

# print(get_conversion_factor.invoke({'base_currency':'USD', 'target_currency':'INR'}))

@tool
def convert(base_currency_amount: int, conversion_rate: float) -> float:
    """this function calculates the target currency from given conversion rate and amount of base currency user want to convert """
    return base_currency_amount*conversion_rate

# print(convert.invoke({'base_currency_value':10, 'conversion_rate':96.0317}))

llm = ChatGroq(model='openai/gpt-oss-20b')
llm_with_tools = llm.bind_tools([get_conversion_factor,convert])

query=input('Enter your query -> ')
messages = [HumanMessage(query)]
ai_message = llm_with_tools.invoke(messages)
print(f"first ai message -> {ai_message} \n\n")
messages.append(ai_message)
for tool in ai_message.tool_calls:
    if tool['name']=='get_conversion_factor':
        tool_message = get_conversion_factor.invoke(tool)
        print(f"first tool message -> {tool_message} \n\n")
        messages.append(tool_message)
        ai_message2=llm_with_tools.invoke(messages)
        print(f"second ai message -> {ai_message2} \n\n")
        messages.append(ai_message2)
        for tool2 in ai_message2.tool_calls:
            if tool2['name']=='convert':
                tool_message2 = convert.invoke(tool2)
                print(f"second tool message -> {tool_message2}\n\n")
                messages.append(tool_message2)
                ai_message3=llm_with_tools.invoke(messages)
                print(ai_message3.content)


