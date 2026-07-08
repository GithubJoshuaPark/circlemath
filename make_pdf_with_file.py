#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys

import nbformat
from nbconvert import WebPDFExporter


def make_pdf(input_path: str, output_path: str = None) -> str:
    """Jupyter Notebook (.ipynb) 혹은 Python (.py) 파일을 PDF로 변환하여 저장합니다.
    
    Args:
        input_path (str): 변환할 대상 파일의 경로 (.ipynb 또는 .py).
        output_path (str, optional): 저장될 PDF 파일의 경로. 생략할 경우 원본 파일 이름의 .pdf로 지정됩니다.
        
    Returns:
        str: 생성 완료된 PDF 파일의 절대 경로.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"입력 파일을 찾을 수 없습니다: {input_path}")
        
    ext = os.path.splitext(input_path)[1].lower()
    
    if not output_path:
        output_path = os.path.splitext(input_path)[0] + ".pdf"
        
    print(f"[PDF 변환] 입력 파일: {input_path}")
    
    # 1. 파일 확장자에 따라 Jupyter Notebook Node (nbformat) 빌드
    if ext == ".ipynb":
        with open(input_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
    elif ext == ".py":
        print("[PDF 변환] Python 스크립트 감지. 임시 노트북 구조 생성 중...")
        with open(input_path, "r", encoding="utf-8") as f:
            py_code = f.read()
            
        nb = nbformat.v4.new_notebook()
        
        # VS Code Interactive Window 형식인 '# %%' 기준으로 셀 분할 지원
        cells = []
        raw_cells = py_code.split("# %%")
        for idx, part in enumerate(raw_cells):
            part_stripped = part.strip()
            if not part_stripped:
                continue
            
            # 주석(Comment)만 있는 셀인지 여부와 가독성 고려하여 코드 셀 추가
            cells.append(nbformat.v4.new_code_cell(part_stripped))
            
        nb.cells = cells
    else:
        raise ValueError(f"지원하지 않는 파일 형식입니다 ({ext}). .ipynb 또는 .py 파일만 지원됩니다.")
        
    # 2. nbconvert의 WebPDFExporter를 사용하여 PDF 생성 (Playwright 기반)
    print("[PDF 변환] WebPDFExporter를 사용해 PDF 컴파일 진행 중 (Playwright 동작)...")
    try:
        exporter = WebPDFExporter()
        pdf_data, _ = exporter.from_notebook_node(nb)
        
        # 3. PDF 저장
        with open(output_path, "wb") as f:
            f.write(pdf_data)
            
        print(f"[PDF 변환] 변환 완료! 저장된 경로: {os.path.abspath(output_path)}")
        return os.path.abspath(output_path)
        
    except Exception as e:
        print(f"[PDF 변환] 에러 발생: {str(e)}", file=sys.stderr)
        print("참고: playwright 가 정상 설치 및 브라우저 다운로드(playwright install)가 완료되었는지 확인해 주세요.", file=sys.stderr)
        raise e

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jupyter Notebook (.ipynb) 또는 Python (.py) 파일을 PDF로 변환하는 스크립트입니다.")
    parser.add_argument("input", help="변환할 입력 파일 (.ipynb 또는 .py)")
    parser.add_argument("-o", "--output", help="생성할 PDF 출력 파일명 (기본값: 원본파일명.pdf)", default=None)
    
    args = parser.parse_args()
    
    try:
        make_pdf(args.input, args.output)
    except Exception as e:
        print(f"[오류] 변환에 실패했습니다: {str(e)}", file=sys.stderr)
        sys.exit(1)
