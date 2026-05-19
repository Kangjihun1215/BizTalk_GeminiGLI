import os
from dotenv import load_dotenv
from langchain_upstage import ChatUpstage
from langchain_core.messages import SystemMessage, HumanMessage
from prompts.templates import PROMPTS

# .env 파일 로드
load_dotenv()

class ToneConverter:
    def __init__(self):
        api_key = os.getenv("UPSTAGE_API_KEY")
        if not api_key:
            raise ValueError("UPSTAGE_API_KEY가 설정되지 않았습니다.")
        
        # Solar-Pro2 모델 설정
        self.llm = ChatUpstage(
            model="solar-pro2",
            upstage_api_key=api_key
        )

    async def convert(self, text: str, target_audience: str) -> str:
        if target_audience not in PROMPTS:
            raise ValueError(f"지원하지 않는 수신 대상입니다: {target_audience}")
        
        system_prompt = PROMPTS[target_audience]
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=text)
        ]
        
        response = await self.llm.ainvoke(messages)
        return response.content

# 싱글톤 인스턴스 생성
converter = ToneConverter()
