from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant")

@tool
def sum(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b

@tool
def multi(a: int, b: int) -> int:
    """Returns the product of two integers."""
    return a * b

messages = []

llm_with_tool = llm.bind_tools([sum, multi])

messages.append(HumanMessage(content="What is the division of 5 and 7?"))

AI = llm_with_tool.invoke(messages)

messages.append(AI)

tool_call = AI.tool_calls[0]

tool_message = ToolMessage(
    content=str(tool_call),
    tool_name=tool_call['name'],
    tool_call_id=tool_call['id']
)

messages.append(tool_message)

response = llm_with_tool.invoke(messages)

print(response.content)