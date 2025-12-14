from fastmcp import MCPClient
from client.cli_interface import run_cli

client = MCPClient("http://127.0.0.1:8000")

if __name__ == "__main__":
    run_cli(client.get_tools())