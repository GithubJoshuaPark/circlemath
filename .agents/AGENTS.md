# Workspace Customizations (circlemath Project Rules)

이 문서는 이 프로젝트(circlemath)에서 AI 어시스턴트(Gemini 등)가 반드시 준수해야 하는 작업 규칙을 정의합니다.

## Matplotlib 시각화 폰트 및 글리프 경고 차단 규칙

* **폰트 굵기 경고 방지 (Failed to find font weight bold)**:
  - macOS 환경에서 `matplotlib`을 이용해 차트를 렌더링하거나 주피터 노트북 내 시각화를 그릴 때, 한글 폰트(`AppleGothic`)는 굵은 가중치(`bold`)를 올바르게 인식하지 못해 경고 메시지를 유발합니다.
  - 따라서 모든 `set_title`, `text`, `annotate`, `label` 등 텍스트 출력 파라미터에서는 **`weight="bold"` 옵션을 완전히 배제하거나 `weight="normal"`로 주어** 경고 로그를 차단해야 합니다.

* **이모지 글리프 유실 방지 (Glyph missing for emojis)**:
  - matplotlib 텍스트 필드 내에 유니코드 이모지(`💡`, `⚠️`, `📊` 등)를 삽입하는 경우 글리프 누락 경고가 상시 발생합니다.
  - 차트의 텍스트 공간 내에는 **이모지 문자를 절대 기입하지 않으며, 대신 `[경고]`, `[안내]`와 같은 텍스트 형태로 대체**하여 오류 없는 렌더링을 지향합니다.
