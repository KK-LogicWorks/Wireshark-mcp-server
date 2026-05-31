from mcp.server import Server
from mcp.server.streamable_http import create_streamable_http_app

server = Server("wireshark-mcp")

app = create_streamable_http_app(
    server,
    streamable_http_path="/mcp"
)