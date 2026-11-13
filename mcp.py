from mcp.server.mcpserver import MCPServer

mcp=MCPServer()

@mcp.tool()
def count_letters(text:str,search:str) -> int:
    """
    Count the number of occurrences of a letter in a string.

    Args:
        text (str): The string to search.
        search (str): The letter to count.

    Returns:
        int: The number of occurrences of the letter in the string.
    
    Use this tool when you need to find how many times a substring appears in a text.

    """
    return text.lower().count(search.lower())

@mcp.resource("greeting://{name}")
def get_greeting(name:str) -> str:
    """
    Generate a greeting message for a given name.

    Args:
        name (str): The name to greet.

    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"

@mcp.prompt(
        title="Count Letters Prompt",
)

def count_letters_prompt(text:str,search:str) -> str:
    return f"Count the number of occurrences of the letter '{search}' in the string '{text}'."

if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="127.0.0.1",
        port=8080,
        path="/mcp",
    )