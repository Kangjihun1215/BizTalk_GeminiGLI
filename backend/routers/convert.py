from fastapi import APIRouter, HTTPException
from models.schemas import ConvertRequest, ConvertResponse
from services.tone_converter import converter

router = APIRouter()

@router.post("/convert", response_model=ConvertResponse)
async def convert_tone(request: ConvertRequest):
    try:
        converted_text = await converter.convert(
            text=request.text,
            target_audience=request.target_audience
        )
        return ConvertResponse(
            converted_text=converted_text,
            target_audience=request.target_audience,
            original_text=request.text
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        # 실제 운영 환경에서는 로그를 남겨야 합니다.
        raise HTTPException(status_code=500, detail=f"LLM API 호출 중 오류가 발생했습니다: {str(e)}")
