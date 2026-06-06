# Agentic AI Learning Repository

A comprehensive learning repository demonstrating how to build AI agents using **LangChain** and **Groq LLM**, with examples of tool creation, binding, and agent execution patterns.

## 📋 Overview

This repository is designed as an educational resource to help developers understand:
- **AI Agent Architecture**: Building agents that can reason and take actions
- **Tool Integration**: Creating custom tools and binding them to LLMs
- **Tool Calling**: Managing multi-turn conversations with tool usage
- **Web Search Integration**: Leveraging external search capabilities with agents
- **ReAct Pattern**: Implementing Reasoning + Acting pattern for intelligent decision-making

## 🗂️ Project Structure

```
agentic-ai/
├── ai_agent.py          # Main AI agent with web search capabilities
├── toolkit.py           # Custom toolkit creation example
├── custome_tool.py      # Individual custom tool implementation
├── tool_bind.py         # Tool binding to LLM with conversation flow
├── tools_built.py       # Built-in LangChain tools usage
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## 📁 File Descriptions

### **ai_agent.py**
Main agent implementation that demonstrates a complete AI agent pipeline:
- Uses **Groq's llama-3.1-8b-instant** model for fast LLM inference
- Implements **ReAct (Reasoning + Acting)** pattern from LangSmith hub
- Integrates **DuckDuckGoSearchRun** for web search capabilities
- Accepts user queries and returns intelligent responses based on web data
- **Example**: `'Way to go goa, india tourise place?'` - Agent searches for information and provides relevant answers

### **toolkit.py**
Demonstrates toolkit creation with multiple tools:
- Shows how to group related tools into a **MathToolKit** class
- Implements `@tool` decorated functions (`sum`, `multiply`)
- Demonstrates tool introspection (name, description, args)
- Useful pattern for organizing related functionality

### **custome_tool.py**
Simple custom tool implementation example:
- Creates a single custom tool using `@tool` decorator
- Shows tool invocation using `.invoke()` method
- Demonstrates accessing tool metadata (name, description, args)
- Good starting point for understanding tool creation

### **tool_bind.py**
Advanced tool binding and conversation flow:
- Demonstrates **binding tools to LLM** using `llm.bind_tools()`
- Shows **multi-turn conversation** handling with message history
- Implements tool calling in agent-LLM interaction
- Uses `HumanMessage`, `AIMessage`, and `ToolMessage` types
- Simulates a conversation where LLM decides to use tools and interprets results

### **tools_built.py**
Built-in LangChain tools example:
- Uses **DuckDuckGoSearchRun** from `langchain_community`
- Demonstrates web search with custom descriptions
- Shows verbose output for debugging
- Simple pattern for leveraging existing community tools

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- API Key for Groq (for llama models)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd agentic-ai
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Running Examples

**Run the main agent:**
```bash
python ai_agent.py
```

**Explore custom tools:**
```bash
python custome_tool.py
```

**Test tool binding:**
```bash
python tool_bind.py
```

**Try built-in tools:**
```bash
python tools_built.py
```

**Explore toolkit pattern:**
```bash
python toolkit.py
```

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `langchain` | Core LangChain framework |
| `langchain-core` | Core abstractions and tools |
| `langchain-community` | Community-provided tools and integrations |
| `langchain-groq` | Groq LLM integration |
| `python-dotenv` | Environment variable management |
| `ddgs` | DuckDuckGo search backend |
| `streamlit` | (Optional) For building interactive UIs |

## 🧠 Key Concepts

### 1. **Tools/Functions**
Tools are the actions an agent can take. They're defined using the `@tool` decorator:
```python
@tool
def sum(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b
```

### 2. **Tool Binding**
Binding tools to an LLM enables the model to decide when and how to use them:
```python
llm_with_tools = llm.bind_tools([sum, multiply])
```

### 3. **ReAct Pattern**
Reasoning + Acting loop where the agent:
1. **Reasons** about the user query
2. **Acts** by calling appropriate tools
3. **Observes** the results
4. **Repeats** until the goal is achieved

### 4. **Agent Executor**
Orchestrates the agent loop, managing tool calls and message flow:
```python
agent_executor = AgentExecutor(agent=agent, tools=[search], verbose=True)
```

## 💡 Learning Path

**Beginner:**
1. Start with `custome_tool.py` - Understand basic tool creation
2. Move to `toolkit.py` - Learn tool organization
3. Explore `tools_built.py` - See built-in tools in action

**Intermediate:**
1. Study `tool_bind.py` - Learn tool binding and multi-turn conversations
2. Understand message types and conversation flow
3. Experiment with different tool configurations

**Advanced:**
1. Examine `ai_agent.py` - Full agent implementation
2. Understand ReAct pattern and agent execution
3. Extend with custom tools and prompts from LangSmith hub

## 🔧 Customization Guide

### Adding a New Custom Tool
```python
from langchain_core.tools import tool

@tool
def your_function(param1: str, param2: int) -> str:
    """Clear description of what this tool does."""
    # Your implementation
    return result
```

### Creating a Custom Toolkit
```python
class YourToolKit:
    """A toolkit for your domain."""
    def get_tools(self):
        return [tool1, tool2, tool3]
```

### Using Tools in an Agent
```python
agent = create_react_agent(model, tools=[your_tools], prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=[your_tools], verbose=True)
response = agent_executor.invoke({'input': 'Your query here'})
```

## 🌐 Web Search Integration

The agent uses **DuckDuckGo** for web searches, providing:
- No API key required (unlike Google Search)
- Privacy-focused search
- Reliable for finding current information
- Easy integration through `langchain_community`

## 📝 Example Usage

```python
# Simple example from ai_agent.py
response = agent_executor.invoke({
    'input': 'What are the best beaches in Goa, India?'
})
print(response)
```

The agent will:
1. Understand the query
2. Decide to search the web
3. Retrieve relevant information
4. Synthesize an answer
5. Return a comprehensive response

## 🎯 Use Cases

This codebase can be extended for:
- **Question Answering Systems**: QA bots with web search
- **Research Assistants**: Automated information gathering
- **Data Analysis Agents**: Tools for calculation and analysis
- **Multi-tool Workflows**: Complex tasks requiring multiple steps
- **Interactive Chatbots**: Streamlit-based conversational interfaces

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Groq API](https://console.groq.com/)
- [ReAct Pattern Paper](https://arxiv.org/abs/2210.03629)
- [LangSmith](https://smith.langchain.com/)

## 🤝 Contributing

This is a learning repository. Feel free to:
- Add new tool examples
- Extend with additional integrations
- Improve documentation
- Share your custom implementations

## 📄 License

This repository is provided as-is for educational purposes.

## 📧 Support

For questions or issues:
1. Check the documentation in each file
2. Refer to LangChain official documentation
3. Review example implementations in the repo

---

**Happy Learning! 🚀**

Created as an educational resource for understanding AI agents, tool creation, and LangChain integration patterns.
