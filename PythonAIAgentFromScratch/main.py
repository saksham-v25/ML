# main.py (The Fix)

import os
from dotenv import load_dotenv # Recommended: Load environment variables
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.prompts import ChatPromptTemplate

# Import all tools from the tools.py file
from tools import search_tool, wiki_tool, save_tool

# --- Configuration ---
load_dotenv() # Load GOOGLE_API_KEY from .env file
# Get your API key, defaulting to the placeholder if .env failed
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "YOUR_GOOGLE_API_KEY_HERE")

# Initialize Google Gemini LLM
# NOTE: 'gemini-alpha-1.3' is deprecated. Use 'gemini-2.5-flash' or 'gemini-2.5-pro'
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", # Updated to a current, fast model
    api_key=GOOGLE_API_KEY,
    temperature=0
)

# Combine all tools into a list
tools = [search_tool, wiki_tool, save_tool]

# --- Prompt for the Agent ---
# This system message is crucial for the agent to know its role and how to use the tools
system_prompt = (
    "You are an expert AI research assistant. Your task is to accurately answer user questions. "
    "You MUST use the provided tools (Search, Wikipedia, or Save Notes) to find the most current and relevant information before answering. "
    "If a tool is not useful for the question, answer directly. Be concise and helpful."
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("placeholder", "{chat_history}"), # Placeholder for chat history if you add memory later
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"), # Crucial for the agent's thought process
    ]
)

# --- Create the Tool-Calling Agent and Executor ---
# 1. Create the Agent: This is the reasoning engine
agent = create_tool_calling_agent(llm, tools, prompt)

# 2. Create the Executor: This manages the agent's run cycle (thought -> tool call -> observation -> final answer)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


def main():
    print("🤖 AI Research Assistant Initialized (using gemini-2.5-flash).")
    while True:
        query = input("What can I help you research? ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting AI research assistant.")
            break

        try:
            # Run the Agent Executor instead of the simple LLMChain
            response = agent_executor.invoke({"input": query})
            # The agent's final answer is in the 'output' key
            print("\nAI Response:\n", response["output"])
            print("\n" + "-"*50 + "\n")
        except Exception as e:
            print(f"\n⚠️ An error occurred: {e}")
            print("Please check your API key and model access.")

if __name__ == "__main__":
    main()