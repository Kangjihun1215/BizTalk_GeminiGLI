from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import convert
import os

app = FastAPI(title="BizTone Converter API")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 배포 시 실제 도메인으로 제한 권장
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/health")
async def health_check():
    return {"status": "ok"}

# API 라우터 등록
app.include_router(convert.router, prefix="/api")

# 프론트엔드 정적 파일 서빙 (STEP 3에서 구현할 index.html 대응)
# frontend 디렉토리가 루트에 있으므로 경로 설정 주의
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
