from fastmcp import FastMCP
import random 
import json

mcp = FastMCP("Simple calculator server")

# tool add

@mcp.tool

def add(a: int , b: int) -> int:
    """ add two numbers.
    Args:
        a: first number
        b: second number
    return sum of a and b
    
    """
    return a + b

# resource server information

@mcp.resource("info://server")
def server_info() -> str:
    """"get info about this server"""
    info = {
        "name" : " Simple calculator Server",
        "version" : "1.0.0",
        "tools" : ["add"],
        "author" : "vikram"

    }
    return json.dumps(info,indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
