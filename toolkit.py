from langchain_core.tools import tool

@tool
def sum(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Returns the product of two integers."""
    return a * b


class MathToolKit:
    """A toolkit for basic math operations."""
    def get_tools(self):
        return [sum, multiply]
    
for tool in MathToolKit().get_tools():
    print(f"Tool Name: {tool.name}")
    print(f"Description: {tool.description}")
    print('======================')


