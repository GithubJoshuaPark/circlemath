# 2026-07-04 requirements.txt 의존성 패키지 갱신

이 문서는 PDF 자료 생성 기능(`make_pdf_with_file.py`) 및 Jupyter Notebook 학습 환경에 필요한 라이브러리 지원을 위해 `requirements.txt` 파일을 갱신한 내역을 기록한 문서입니다.

## 1. 개요 및 목적
- 향후 Jupyter Notebook (`.ipynb`) 및 Python 스크립트 (`.py`)를 PDF로 변환하는 자동화 기능([make_pdf_with_file.py](file:///Users/joshuapark/Desktop/Dev/soromiso/circlemath/make_pdf_with_file.py))을 실행하는 데 필요한 라이브러리 환경을 구축합니다.
- 기존에 분리하여 보관 중이던 [requirements copy.txt](file:///Users/joshuapark/Desktop/Dev/soromiso/circlemath/requirements%20copy.txt)의 전체 패키지 목록을 공식 [requirements.txt](file:///Users/joshuapark/Desktop/Dev/soromiso/circlemath/requirements.txt)로 병합 및 갱신하였습니다.

## 2. 주요 변경 사항
- **기존 `requirements.txt` 패키지**: `numpy`, `matplotlib`, `sympy`, `jupyter`, `scipy` 등 5가지 기본 수학/학습 도구 명세만 존재.
- **갱신된 `requirements.txt` 패키지**: 총 129개 패키지의 버전 고정(pinned version) 명세 추가.
  - Jupyter 생태계 관련: `jupyterlab`, `jupyter_server`, `notebook`, `ipykernel` 등
  - PDF 및 변환 관련: `nbconvert` (WebPDFExporter용), `nbformat`, `bleach`, `pandocfilters`, `tinycss2` 등
  - 수치 분석 및 시각화 관련: `numpy==1.26.4`, `pandas==3.0.3`, `scipy==1.17.1`, `matplotlib==3.11.0`, `seaborn==0.13.2`, `sympy==1.14.0` 등
  - 딥러닝/머신러닝 관련: `torch==2.2.2`, `scikit-learn==1.9.0` 등
  - API 및 유틸리티 관련: `fastapi==0.137.1`, `uvicorn==0.49.0`, `httpx==0.28.1`, `pydantic==2.13.4` 등

## 3. 후속 주의 사항 (Playwright 브라우저 관련)
- [make_pdf_with_file.py](file:///Users/joshuapark/Desktop/Dev/soromiso/circlemath/make_pdf_with_file.py)는 `nbconvert.WebPDFExporter`를 사용합니다. 해당 모듈은 내부적으로 Headless Chromium 브라우저를 띄워 HTML을 PDF로 프린트하는 방식(`playwright` 활용)을 사용하므로, 만약 로컬 터미널에서 동작 중 에러가 발생할 경우 아래 명령어를 실행해야 합니다.
  ```bash
  playwright install
  ```
  *(현재 가상환경 또는 전역 패키지에 `playwright` 패키지가 없을 경우 `pip install playwright` 선행 설치 필요)*
