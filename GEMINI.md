# Project - Global Rules (GEMINI)

이 문서는 프로젝트의 일관된 개발 및 디자인 원칙을 정의하며, AI 어시스턴트(Gemini)와의 협업 시 토큰 낭비를 최소화하고 일관된 산출물을 얻기 위해 작성되었습니다.

## 0. 사용자 정체성 및 대화 지침 (User Identity & Interaction Guidelines)

- **사용자 호칭**: "Joshua"이다. 선생님이라는 호칭은 사용하지 말아야 한다.
- **사용자 프로필**: 대한민국 50대 남성, 2000년부터 소프트웨어 개발을 해 온 베테랑 개발자.
- **주요 관심사**: 현재 LLM API를 이용한 SaaS 서비스 개발에 주력 중이며, Web, App 개발, Database, Biz Process 설계에 여전히 높은 관심을 가짐.
- **언어 및 어조**: 한국어로 대답할 때는 **반드시 존댓말(존칭)**을 사용해야 한다.

## 1. 가장 중요: 답변 기록 필수 규칙 (Highest Priority)

어떤 답변이나 코드 구현 내역, 분석 결과, 설명 등을 Joshua에게 전달할 때는 **반드시** 이 내용을 요약한 Markdown 파일을 `doc_fr_llm` 디렉토리에 저장해야 합니다.

- **파일명 규칙**: `doc_fr_llm/yyyymmdd_HHMMSS_제목.md` (예: `doc_fr_llm/20240414_154500_기억장치규칙추가.md`)
- **이유**: Joshua님이 언제든 과거의 논의 내역과 답변을 쉽게 찾아보고 참조할 수 있도록 하기 위함입니다.
- 답변을 제공함과 동시에 해당 파일을 File System에 명시적으로 생성하고 내용을 작성해야 합니다.

## 2. Token Economy (경제적인 토큰 사용 원칙)

1인 개발 환경에서 생산성을 유지하며 토큰 소모를 최소화하기 위한 가이드라인이다.

- **Selective Context (선택적 컨텍스트 제공)**: 파일 전체를 첨부하기보다 `@` 기호나 특정 라인 범위(`:L10-L50`)를 사용하여 반드시 필요한 부분만 AI에게 전달한다.
- **Incremental Tasks (단계적 작업 분할)**: "앱 전체 리팩토링" 같은 거대한 요청 대신, "A 컴포넌트의 스타일 수정", "B 함수의 로직 개선" 등 작고 명확한 단위로 나누어 요청한다. 이는 AI의 정확도를 높이고 불필요한 재작업을 줄인다.
- **Efficient Discovery (효율적인 탐색 도구 활용)**: 파일 내용을 확인하기 전 `grep` 검색이나 `list_dir`을 먼저 사용하여 필요한 파일만 콕 집어서 읽는다.
- **Graphify Context (지식 그래프 기반 분석)**: [NEW] 프로젝트의 거시적 구조나 복잡한 의존성 분석 시 `graphify-out/` 내 산출물을 우선 참조한다.
  - `GRAPH_REPORT.md`를 먼저 읽어 핵심 노드, 의존성 관계, 추천 질문을 파악하여 탐색 범위를 좁힌다.
  - `graphify query/explain/path` 명령어를 Antigravity에게 실행하도록 지시하여 필요한 맥락만 '핀포인트'로 추출하게 함으로써 토큰 소모를 최소화한다.
- **RTK Context (로그 및 출력 토큰 최적화)**: 터미널 명령어(테스트 수행, 디렉토리 탐색 등)의 결과값이 길어질 것 같을 때, 전역 범위로 설정된 `rtk` 훅에 의해 자동 압축됨을 인지하고 AI가 이를 적극 활용하여 불필요한 토큰 낭비를 절감한다.
- **Knowledge Leverage (문서화 활용)**: `README.md`, `ERD.md`를 최신으로 유지하면 AI가 전체 코드를 훑지 않고도 프로젝트 구조를 즉시 파악할 수 있어 토큰이 대폭 절약된다.
- **Model Tiering (모델 계층별 활용)**:
  - 단순 오타 수정, 스타일 조정, 코드 설명 등은 `Gemini 1.5 Flash` 같은 가벼운 모델을 사용합니다.
  - 복잡한 로직 설계, 난해한 버그 추적, 아키텍처 변경 시에만 고성능 모델을 사용하도록 전환합니다.
- **Clear & Concise Prompting (명확하고 간결한 지시)**: 배경 설명은 최소화하되, 얻고자 하는 결과물(Output)의 형태를 구체적으로 지정하여 불필요한 대화 루프를 방지합니다.

## 3. AI 어시스턴트 (Gemini) 행동 지침 🚨

- **SequentialThinking 사용 금지**: 매우 복잡한 아키텍처 설계나 난해한 디버깅이 아닌 이상 `SequentialThinking` MCP 도구의 사용을 배제합니다. 불필요한 토큰 낭비와 응답 딜레이를 방지하기 위해 직관적이고 빠른 내장 기본 논리력으로 바로 코드를 작성합니다.
- **간결하고 명확한 답변**: 불필요하게 긴 설명이나 장황한 과정 나열을 생략하고, 즉시 적용 가능한 결과물(Code)과 핵심 요약만 제공합니다.
- **Proactive UX Improvement (주도적인 UX 개선)**: 요구사항을 구현할 때, 지시하지 않더라도 모바일 패딩, 글꼴 크기 혼선, 버튼 클릭 영역 등 발견되는 UI/UX 이슈는 주도적으로 전문가 수준에 맞춰 수정(Refining)합니다.
- **수정 사항 연속성 유지**: 기존에 작성해 둔 디자인 시스템(`index.css`의 토큰, 컴포넌트 구조 등)을 파괴하지 않고, 기존 규칙을 계승하면서 코드를 전개합니다.
- **LLM 모델명 검증 철저 (Model Validation First)**: 향후 LLM 관련 API(Gemini, OpenAI 등)를 호출하는 새로운 함수를 작성하거나 기존 코드를 수정할 때는, 소스 코드를 생성하기 전에 **반드시** 현재 프로젝트 환경 및 API Key에서 실제로 사용 가능한 정확한 모델명인지 선제적으로 확인(예: 공식 문서 확인 또는 `ai.models.list` 테스트 스크립트 실행 등)해야 합니다. 임의의 모델명이나 지원되지 않는 최신/프리뷰 버전을 임의로 추측하여 작성하는 것을 엄격히 금지합니다.

## 4. 핵심 디자인 원칙 (Premium UI/UX)

- **Aesthetic (미적 방향성)**: "Mission Control" (상황실) 컨셉. 전문가 수준의 신뢰감과 세련미를 주는 밝고(Bright) 프리미엄한 디자인. 다소 어둡거나 칙칙한 테마는 지양합니다.
- **Color System**: 로고 기반의 `Blue (#0B79D0)` 👉 `Green (#2FA85D)` 대각선 그라데이션이 핵심입니다. CSS 변수(`var(--brand-gradient)`, `var(--brand-primary)`, `var(--brand-secondary)`)를 적극 활용합니다.
- **Glassmorphism (글래스모피즘)**: `backdrop-filter: blur()`, 반투명 배경(`rgba(255,255,255,0.x)`), 부드러운 그림자를 사용하여 깊이감 있는 세련된 UI를 구성합니다. (`premium-card`, `glass-card`, `glass-btn` 클래스 활용)
- **Mobile First & Responsive**: 모바일 기기에서의 시인성과 터치 편의성을 최우선으로 고려합니다.
  - 글꼴 크기는 `clamp()`를 사용하여 유연하게(Fluid) 대응합니다.
  - 모바일 버튼 및 입력창의 높이는 터치하기 쉽게 충분히 확보합니다 (예: 56px ~ 64px).
- **Micro-interactions**: 호버(Hover) 효과, 상태 변화 애니메이션(FadeIn, Slide 등), 화려하지 않으면서도 고급스러운 요소(Mesh Background, Floating 요소)를 적절히 배치합니다.

## 5. 기술 스택 및 코드 작성 컨벤션

- **Core**: React, TypeScript, React Router DOM
- **Styling**: 디자인 시스템의 토큰(CSS 변수)과 공통 클래스는 `index.css`에 직접 정의하여 사용하고, 레이아웃(`flex`, `grid`, 여백 등)에는 제한적으로 Tailwind CSS 유틸리티를 병행하여 효율성을 높입니다.
- **Component Structure**: 함수형 컴포넌트와 React Hooks를 사용하며, 중복되는 로직이나 UI는 분리하여 재사용성을 극대화합니다.

## 6. Modal / Popup Component Rules (모달 제작 원칙)

- **공통 스타일링 (Glassmorphism)**: 자체적인 인라인 스타일을 남발하지 않고, `index.css`에 직접 정의된 `.auth-modal-overlay` (배경) 및 `.glass-panel` (본체) 클래스를 사용하여 일관된 투명도와 블러(Blur) 효과를 부여합니다.
- **배치 및 중앙 정렬 (Positioning)**: `.auth-modal-overlay`는 기본적으로 `position: fixed`, `display: flex`, `align-items: center`, `justify-content: center` 동작을 보장힙니다. **절대 인라인으로 불필요한 높이/너비/정렬 스타일 속성을 덧대지 마세요.**
- **⚠️ Transform 충돌 방지 (중요)**: 모달 컴포넌트를 렌더링할 때, 모달을 감싸는 부모 컨테이너에 CSS `transform` 속성(예: `animate-fadeInUp`, `animate-slideInRight` 등)이 적용되어 있으면, 브라우저 스펙상 `position: fixed`가 뷰포트를 기준으로 하지 않고 해당 부모를 기준으로 렌더링되어 위치가 화면 하단으로 쏠리거나 깨지는 부작용이 발생합니다. 따라서 **오버레이 모달 컴포넌트는 반드시 CSS `transform`이 없는 곳(최상단 레벨 또는 형제(Sibling) 요소)으로 완전히 분리해 배치**해야 합니다 (필요 시 React Portal 사용).

## 7. 문서 동기화 강제 (Mandatory Document Synchronization)

- 프로젝트 내 코드 변경, 기능 추가, 삭제, 필드 병합 등 아키텍처나 기능에 변경이 발생할 경우, **반드시 `README.md`와 `documents/ERD.md` 이 2개의 문서를 즉각적으로 동시에 업데이트(동기화)** 해야 합니다.
- 프로젝트 내 코드 변경, 기능 추가, 삭제, 필드 병합 등 아키텍처나 기능에 변경이 발생할 경우, **반드시 `sh scripts/update_graph.sh`를 실행하여 지식 그래프를 갱신해야 합니다.**
- 어떤 AI 에이전트가 작업을 하든, 기존의 컨텍스트를 상실하지 않도록 히스토리와 ERD 명세를 최신화하는 것을 최우선 규칙으로 삼습니다.
- `doc_fr_llm` 폴더는 Git 추적에서 제외합니다.

## 8. Jupyter Notebook 및 소스 코드 작성 하는 경우의 지침 (Python & Jupyter)

- **코드 생성 주석 상세화 (Detailing Comments)**:
  - 파이썬 초보자가 읽더라도 이해할 수 있도록 코드의 줄마다 최대한 상세하고 친절한 한국어 주석을 달아야 합니다.
  - 단순한 코드 요약에 그치지 않고, 라이브러리를 가져오는 목적, 수학적 공식의 파이썬 구현 로직, 반복문/조건문의 필터링 이유, 시각화 스타일(색상, 테두리, 뷰포트 고정 등)의 기하학적/브랜드 의도 등을 라인별로 구체적으로 설명해야 합니다.
- **노트북 셀 세분화 및 설계 (Cell Splitting)**:
  - 하나의 코드 셀에 대량의 연산이나 로직을 몰아넣지 않고, 기능적 단위별로 최소 3개 이상의 코드 셀로 쪼개어 설계합니다.
  - 일반적인 구성 흐름:
    1. **[도구 준비 셀] (Imports & Settings)**: 라이브러리 임포트 및 OS별 한글 깨짐 방지 폰트/마이너스 기호 설정.
    2. **[수학적 데이터 생성 셀] (Data Generation & Functions)**: 수학적/논리적 함수 정의 및 데이터 셋 생성(순수 연산/가공 로직).
    3. **[시각화 렌더링 셀] (Plotting & Execution)**: matplotlib/networkx 등을 활용한 디자인 렌더링 및 실행 지시.
    4. **[인터랙티브 / 미디어 셀] (Interaction & Media)**: ipywidgets 슬라이더나 오디오 재생 등 인터랙티브 테스트 수행.
  - 코드 셀의 사이사이에는 초보자가 흐름과 논리를 차분히 읽을 수 있도록 해설 목적의 마크다운 셀(Markdown Cell)을 풍성하게 배치해야 합니다.

