from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool

# ----------------------------
# 1. DuckDuckGo Search Tool
# ----------------------------
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Useful for searching the internet when the user asks about current events, news, or general information."
)

# ----------------------------
# 2. Wikipedia Tool
# ----------------------------
wiki = WikipediaAPIWrapper()
wiki_tool = Tool(
    name="Wikipedia",
    func=wiki.run,
    description="Use this when the user asks about factual, encyclopedic knowledge."
)

# ----------------------------
# 3. Save Notes Tool
# ----------------------------
def save_notes(text: str, filename: str = "notes.txt") -> str:
    """
    Save text into a local file (notes.txt by default).
    """
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(text + "\n")
        return f"✅ Notes saved successfully to {filename}."
    except Exception as e:
        return f"⚠️ Error saving notes: {str(e)}"

save_tool = Tool(
    name="Save_Notes",
    func=save_notes,
    description="Use this tool to save important text or user notes into a local file."
)

# ----------------------------
# Export Tools
# ----------------------------
__all__ = ["search_tool", "wiki_tool", "save_tool"]
