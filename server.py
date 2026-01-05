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

@mcp.tool
def make_morning_briefing(sleep_start: str, sleep_end: str) -> str:
    """
    수면 구간을 받아 '당신이 잠든 사이' 브리핑 텍스트를 생성합니다.
    예: "2026-01-05 00:30", "2026-01-05 07:10"
    """
    return (
        "🌙 당신이 잠든 사이 브리핑\n"
        f"- 수면 구간: {sleep_start} ~ {sleep_end} (Asia/Seoul)\n\n"
        "📈 밤사이 경제 뉴스 TOP\n"
        "1) (MVP) 아직 뉴스 수집 연결 전\n"
        "2) (MVP) 아직 뉴스 수집 연결 전\n"
        "3) (MVP) 아직 뉴스 수집 연결 전\n\n"
        "💬 중요한 카톡 요약\n"
        "- (MVP) 아직 메시지 읽기/선별 연결 전\n\n"
        "✅ 오늘 한 줄 액션\n"
        "- (MVP) 내일은 ‘주요 이슈 3줄 + 영향(원달러/코스피/미국선물)’까지 넣자"
    )

if __name__ == "__main__":
    # PlayMCP 같은 “remote 등록”은 HTTP가 정석
    port = int(os.environ.get("PORT", "8000"))
    mcp.run(transport="http", host="0.0.0.0", port=port)



