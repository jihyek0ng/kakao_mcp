import os
from fastmcp import FastMCP
from starlette.responses import PlainTextResponse
from starlette.requests import Request

mcp = FastMCP("while-you-were-asleep")

@mcp.tool
def ping() -> str:
    """서버 연결 확인용 ping"""
    return "pong"

@mcp.custom_route("/health", methods=["GET"])
async def health(_: Request):
    return PlainTextResponse("OK")

if __name__ == "__main__":
    # PlayMCP 같은 “remote 등록”은 HTTP가 정석
    port = int(os.environ.get("PORT", "8000"))
    mcp.run(transport="http", host="0.0.0.0", port=port)
