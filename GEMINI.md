# Gemini Project Rules: circlemath (50대의 수학 학습 Retreat) (GEMINI.md)

이 문서는 `circlemath` 프로젝트의 고유한 개발 지침과 디자인 원칙을 정의합니다.
본 지침은 전역 Rule(`~/.gemini/GEMINI.md`)을 기본으로 따르되, 본 프로젝트의 모든 작업은 이 파일의 명세를 최우선으로 준수합니다.

## 1. 기술 스택 (Core Tech Stack)

- **Frontend**: React 19 (Vite), TypeScript, React Router DOM v7
- **Backend (Firebase)**:
  - **Auth**: Google Social & Email/Password Login
  - **Firestore**: User Profile (`user_profile`) 및 정적 조직 정보
  - **Realtime Database (RTDB)**: 수학 학습 Retreat 일정(`circle_lessons`), 메모/피드(`circle_notes`), 다국어데이터(`circle_translations`)
  - **Functions**: 서비스 관리(Admin), 연쇄 삭제, 데이터 시딩 전문 함수
- **Styling**: Vanilla CSS (Design Tokens) + Tailwind CSS (Layout helper)
- **PWA**: Service Worker (`sw.js`) 기반 오프라인 캐싱 및 모바일 설치 지원

## 2. 디자인 시스템: Anti-Brutalism (안티 브루탈리즘)

전역 디자인 철학인 "Mission Control"을 `circle`만의 안티 브루탈리즘 양식으로 구체화합니다.

### 🎨 Color Palette & Typography

- **Primary**: Stark Red (`#ff5a5f`) - 핵심 동작 버튼
- **Secondary**: Vibrant Yellow (`#ffd166`) - 강조 및 포인트
- **Accent**: Bright Green (`#06d6a0`) - 성공 상태 및 긍정 요소
- **Typography**: "LG Smart" 폰트를 사용하며, 제목(h1~h4)은 Bold(800)와 대문자(Uppercase)를 선호합니다.

### 💎 UI/UX 요소 (Premium Brutalism)

- **Shadow**: 부드러운 빛 대신 **4px/6px의 딱딱한 오프셋 그림자**(`--shadow-brutal`)를 사용합니다.
- **Border**: 모든 인터랙티브 요소는 **3px 검정 실선**(`--border-thick`)으로 경계를 명확히 합니다.
- **Micro-interactions**: 호버 시 그림자 확대, 클릭 시 `translate(2px, 2px)`와 그림자 축소를 통해 물리적인 눌림 효과를 부여합니다.
- **Layout**: 모바일 전용 앱 느낌을 위해 `#root`의 최대 너비를 **480px**로 고정하고 중앙 정렬합니다.

## 3. Firebase 및 데이터 컨벤션

### 📂 데이터 저장소 분리 정책

- **Firestore**: 프로필(`user_profile`) 등 영구적이고 정형화된 데이터.
- **RTDB**: 수학 학습 Retreat 학습 일정(`circle_lessons`), 공지사항(`circle_notice`), 실시간 메모/댓글(`circle_notes`), 다국어데이터(`circle_translations`) 등 빈번한 업데이트가 필요한 데이터.

### 🤖 Firebase MCP 우선 사용 (Firebase MCP First)

Firebase 관련 작업 수행 시, **반드시 Firebase MCP를 통해** 스키마와 규칙을 먼저 확인합니다.

1. `firebase_get_environment`로 현재 프로젝트 디렉토리 확인.
2. 디렉토리가 다를 경우 `firebase_update_environment(project_dir: "<root>")` 실행.
3. `.firebaserc`의 `active_project`(Project ID) 명세 일치 여부 검증 필수.

### 📸 이미지 업로드 및 보안

- **이미지 압축**: `image/*` 파일 업로드 시 반드시 `browser-image-compression`을 사용하여 압축 처리합니다. (`maxSizeMB: 0.5`, `maxWidthOrHeight: 800`)
- **Admin 패턴**: 쓰기 작업은 클라이언트 직접 접근보다 Cloud Functions(`httpsCallable`)을 경유하는 것을 지향합니다.

## 4. 프로젝트 관리 및 작업 규칙

- **Mobile First**: 모든 컴포넌트는 모바일 세로 화면을 기준으로 설계하며, 터치 영역(최소 56px 이상)을 충분히 확보합니다.
- **i18n**: UI 텍스트는 `src/i18n` 컨테스트를 사용하며, 신규 텍스트 추가 시 한/영 데이터를 모두 업데이트합니다.
- **문서 동기화 (Mandatory)**:
  - 코드 변경 시 `README.md`와 `documents/ERD.md`를 즉시 동기화합니다.
  - 주요 기능 구현 후 `sh scripts/update_graph.sh`를 실행하여 지식 그래프를 갱신합니다.
- **분석 스킬**: 프로젝트 구조 파악 시 `doc_fr_llm/skills/graphify_skill.md`를 우선 참조하여 토큰 효율을 높입니다.

---

**최종 업데이트**: 2026-07-05 (circlemath)
