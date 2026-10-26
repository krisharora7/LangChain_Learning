from langchain_community.tools import DuckDuckGoSearchRun, ShellTool
''' duck duck go search tool ->'''
def search(query :str) -> str:
    search_tool = DuckDuckGoSearchRun()
    result = search_tool.invoke(query)
    return result


''' shell search tool ->'''
def shell(query :str) -> str:
    shell_tool = ShellTool()
    result = shell_tool.invoke(query)
    return result

print(shell('whoami'))