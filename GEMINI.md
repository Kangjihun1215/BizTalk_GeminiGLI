# 업무 말투 변환기 (BizTone Converter) - Project Instructions

이 프로젝트는 Upstage Solar-Pro2 모델을 활용하여 사용자의 입력을 다양한 수신 대상(상사, 동료, 고객 등)에 적절한 업무용 말투로 변환해주는 서비스입니다.

## 🚀 프로젝트 개요 (Project Overview)

- **목적**: 비즈니스 커뮤니케이션에서 표현의 어려움을 겪는 사용자들을 위해 AI가 상황에 맞는 적절한 업무 언어로 변환 제공.
- **핵심 기술**:
  - **Backend**: Python 3.11+, FastAPI, LangChain, `langchain-upstage`
  - **Frontend**: HTML5, CSS3, JavaScript (Vanilla JS)
  - **AI Model**: Upstage Solar-Pro2
  - **Infrastructure**: Vercel (Frontend 배포), GitHub
- **아키텍처**:
  ```
  [Frontend: HTML/JS] <-> [Backend: FastAPI] <-> [AI: Upstage Solar-Pro2]
  ```

## 🛠️ 실행 및 개발 가이드 (Building and Running)

### 사전 요구 사항
- Python 3.11 이상
- Upstage API Key (`UPSTAGE_API_KEY`)

### 백엔드 (Backend) 설정 및 실행
1. `backend` 디렉토리로 이동합니다.
2. 가상환경 생성 및 활성화:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. 패키지 설치:
   ```bash
   pip install -r requirements.txt
   ```
4. `.env` 파일 생성 (API 키 설정):
   ```bash
   UPSTAGE_API_KEY=your_api_key_here
   ```
5. 서버 실행:
   ```bash
   uvicorn main:app --reload
   ```

### 프론트엔드 (Frontend) 실행
- `frontend/index.html` 파일을 브라우저에서 직접 열거나, VS Code의 Live Server 확장을 사용하여 실행합니다.

## 📏 개발 규칙 (Development Conventions)

### 1. 바이브 코딩 (Vibe Coding) 3원칙 준수
- **원칙 1. 완료 기준 정의**: 작업을 시작하기 전에 `PRD_업무말투변환기.md`의 체크리스트를 확인하고 목표를 명확히 합니다.
- **원칙 2. 조사 먼저, 구현 나중**: 새로운 라이브러리나 API 도입 시 연동 방식을 먼저 파악한 후 코드를 작성합니다.
- **원칙 3. 버그 분석 우선**: 에러 발생 시 원인 분석을 먼저 수행하고, AI에게 원인 설명을 요구한 뒤 수정을 진행합니다.

### 2. 코드 스타일 및 아키텍처
- **Surgical Updates**: 기존 코드를 수정할 때는 최소한의 범위만 정확하게 변경합니다.
- **Type Safety**: Pydantic 모델(`schemas.py`)을 사용하여 요청/응답 데이터의 유효성을 검증합니다.
- **CORS**: 프론트엔드와 백엔드의 통신을 위해 `CORSMiddleware` 설정을 항상 확인합니다.

### 3. 보안
- `.env` 파일은 절대 Git에 커밋하지 않습니다. (`.gitignore` 확인 필수)
- API 키나 민감한 정보가 로그나 코드에 노출되지 않도록 주의합니다.

## 📂 주요 파일 구조 (Key Files)
- `backend/main.py`: FastAPI 앱 진입점 및 미들웨어 설정.
- `backend/services/tone_converter.py`: LangChain과 Upstage 모델 연동 로직.
- `backend/prompts/templates.py`: 수신 대상별 프롬프트 정의.
- `frontend/js/app.js`: API 호출 및 화면 렌더링 로직.
- `PRD_업무말투변환기.md`: 제품 요구사항 및 상세 명세 (가장 중요한 참조 문서).
- `개요서_업무말투변환기.md`: 프로젝트 목적 및 비즈니스 배경.

## 📝 TODO / 향후 과제
- [ ] 실제 `backend` 및 `frontend` 디렉토리 내 소스 코드 구현 완료 (현재 구조 기반)
- [ ] Vercel 배포 설정 (`vercel.json` 등)
- [ ] (선택) 로그인 및 변환 이력 저장 기능 추가

---
### Source Code가 변경되거나 라이브러리 버전이 변경되면 반드시 @PRD_업무말투변환기.md 문서도 반드시 같이 업데이트 합니다.
* 구현이 완료된 사항들은 완료 체크리스트에 모두 체크표시를 해서 완료되었음을 표시하세요.