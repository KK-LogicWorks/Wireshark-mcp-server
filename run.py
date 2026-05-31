import argparse
import uvicorn

from app.server import mcp


parser = argparse.ArgumentParser()

parser.add_argument(
    "--transport",
    choices=["stdio", "http"],
    default="stdio"
)

args = parser.parse_args()


if args.transport == "stdio":

    try:
        mcp.run()

    except KeyboardInterrupt:
        print("\nMCP server stopped gracefully.")


elif args.transport == "http":

    uvicorn.run(
        "app.transports.http_transport:app",
        host="0.0.0.0",
        port=8080,
        reload=False
    )