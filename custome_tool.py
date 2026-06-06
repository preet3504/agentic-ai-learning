from langchain_core.tools import tool

# Custom tool example
@tool
def sum(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


# Example usage of the custom tool
result = sum.invoke({"a": 5, "b": 7})
print("The sum is:", result)
print(sum.name)
print(sum.description)
print(sum.args)
