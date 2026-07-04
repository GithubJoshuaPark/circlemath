---
name: graphify
description: sorotrip 프로젝트의 Graphify 지식 그래프를 활용하여 코드베이스의 상호작용과 의존성을 분석하는 전문가 스킬입니다.
---

# [Skill] sorotrip Graphify Codebase Expert

이 파일은 AI 어시스턴트가 `sorotrip` 프로젝트를 분석할 때 Graphify를 우선 활용하도록 돕는 프로젝트 맞춤형 Skill입니다.

## 1. 목적

`sorotrip`는 여행 일정/장소 중심 기능에 메모, 댓글, 좋아요, 알림, AI 생성 기능이 결합된 서비스형 프로젝트입니다.
이 Skill의 목적은 Graphify를 통해 **여행 기능군과 소셜/상호작용 기능군, 그리고 AI 기능의 연결 구조를 빠르게 파악하고 토큰 사용을 줄이는 것**입니다.

## 2. 우선적으로 Graphify를 써야 하는 상황

- 일정 / 장소 / 메모 흐름을 파악할 때
- 댓글 / 좋아요 / 알림 상호작용 구조를 볼 때
- 인증 흐름과 사용자 프로필 연결을 분석할 때
- AI 생성 기능이 실제 사용자 기능과 어떻게 연결되는지 볼 때
- 여행 기능군과 소셜 기능군의 경계를 정리할 때

## 3. 프로젝트 핵심 기능 축

Graphify로 볼 때 우선 주목할 축은 아래입니다.

1. 인증 / 사용자 프로필
2. 여행 일정 / 장소 데이터
3. 메모 저장 / 삭제 / 이미지 처리
4. 댓글 기능
5. 좋아요 / 알림 기능
6. AI 생성 기능 (음악 / 이미지 / 문장 / 오디오)
7. Firebase 기반 서비스 연결

## 4. 우선 확인 리소스

1. `graphify-out/GRAPH_REPORT.md`
2. `graphify-out/graph.json`
3. 필요 시 `README.md`, `documents/graphify.md`

## 5. 핵심 명령어

- 그래프 갱신: `sh scripts/update_graph.sh`
- 구조 질문: `graphify query "질문 내용"`
- 노드 설명: `graphify explain "노드명"`
- 경로 추적: `graphify path "출발지" "목적지"`

## 6. 질문 템플릿 예시

- `graphify query "메모, 댓글, 알림의 연결 구조 설명"`
- `graphify path "CommentSection" "createNotification()"`
- `graphify explain "generateAndStoreMusicWithLyrics()"`
- `graphify query "여행 기능군과 소셜 기능군의 경계 설명"`

## 7. 실행 지침

1. 먼저 `GRAPH_REPORT.md`에서 인증, 메모, 댓글, 알림, AI 커뮤니티를 확인한다.
2. 여행 기능군과 소셜 기능군 중 질문의 중심이 어디인지 먼저 분류한다.
3. 이후 `query`, `explain`, `path`로 관련 기능군만 정밀 분석한다.
4. 실제 코드 열람은 관련 페이지, 서비스, Firebase 연결 파일만 최소한으로 수행한다.
5. 답변 시 “인증 / 여행 / 메모 / 댓글 / 좋아요 / 알림 / AI” 중 어떤 축의 문제인지 먼저 명확히 한다.

## 8. 주의사항

- `sorotrip`는 단일 도메인 앱이 아니라 여행 + 소셜 + AI 기능이 혼합된 구조이므로, 기능군 구분이 중요하다.
- Graphify상 AI 생성 기능의 존재감이 커 보일 수 있으므로, 실제 사용자 흐름과 얼마나 연결되는지도 함께 판단한다.
- Firebase 서비스가 여러 축에 걸쳐 있으므로, 경로 추적 없이 무작정 전체 서비스를 읽지 않는다.

---

**Skill 등록일**: 2026-04-19
**버전**: 1.1.0
