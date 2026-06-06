# Build-in tools example 

from langchain_community.tools import DuckDuckGoSearchRun

# Use the DuckDuckGoSearchRun tool to perform a web search
tool = DuckDuckGoSearchRun(
    description="A custom DuckDuckGo search tool for finding programming resources.",
    verbose=True
)

# Example usage
result = tool.invoke("What is the current date?")

word_count = len(result.split())
print("\nNumber of words:", word_count)
print(result)