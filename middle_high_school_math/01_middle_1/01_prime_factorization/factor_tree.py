import matplotlib.pyplot as plt

# 한글 폰트 설정 (추가됨)
import platform

if platform.system() == "Darwin":  # Mac
    plt.rcParams["font.family"] = "AppleGothic"
elif platform.system() == "Windows":  # Windows
    plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

def get_factor_tree(n):
    """
    재귀적으로 소인수분해 트리 구조를 생성하는 함수
    반환 값: (현재값, 왼쪽자식, 오른쪽자식)
    """
    if n < 2:
        return (n, None, None)
    
    # 가장 작은 약수(소수) 찾기
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # i는 소수, n//i는 다음 분할 대상
            left = (i, None, None)  # 소수 노드는 단말 노드
            right = get_factor_tree(n // i)
            return (n, left, right)
            
    # 자기 자신이 소수인 경우
    return (n, None, None)

def build_tree_layout(node, x, y, dx, dy, points, lines, labels):
    """
    트리 노드들의 기하학적 좌표를 계산하는 재귀 함수
    """
    val, left, right = node
    # 현재 노드 위치 기록
    points.append((x, y))
    labels.append(str(val))
    
    # 단말 노드가 아니면 하위 자식 노드 전개
    if left is not None and right is not None:
        # 왼쪽 자식 노드 좌표 계산 (아래 및 왼쪽으로 이동)
        lx, ly = x - dx, y - dy
        lines.append(((x, lx), (y, ly)))
        build_tree_layout(left, lx, ly, dx * 0.5, dy, points, lines, labels)
        
        # 오른쪽 자식 노드 좌표 계산 (아래 및 오른쪽으로 이동)
        rx, ry = x + dx, y - dy
        lines.append(((x, rx), (y, ry)))
        build_tree_layout(right, rx, ry, dx * 0.5, dy, points, lines, labels)

def plot_factor_tree(number):
    """소인수분해 과정을 트리 형태로 시각화하는 함수"""
    if number < 2:
        print("2 이상의 자연수를 입력해 주세요.")
        return
        
    tree = get_factor_tree(number)
    
    points = []
    lines = []
    labels = []
    
    # 레이아웃 좌표 초기화 및 계산
    build_tree_layout(tree, x=0.0, y=0.0, dx=2.0, dy=1.0, points=points, lines=lines, labels=labels)
    
    plt.figure(figsize=(10, 8), facecolor='#0D1117')  # Premium Dark Theme
    ax = plt.subplot(111)
    ax.set_facecolor('#0D1117')
    
    # 1. 트리 가지(선) 그리기
    for line in lines:
        xs, ys = line
        ax.plot(xs, ys, color='#8B949E', linewidth=2, zorder=1)
        
    # 2. 노드(점)와 라벨 그리기
    for (px, py), label in zip(points, labels):
        # 소수(단말 노드)는 초록색, 합성수(중간 노드)는 파란색
        is_prime_leaf = label in ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29", "31"] or int(label) < 100 and all(int(label) % i != 0 for i in range(2, int(int(label)**0.5)+1))
        
        node_color = '#2FA85D' if is_prime_leaf else '#0B79D0'
        edge_color = 'white' if is_prime_leaf else '#8B949E'
        
        # 원형 노드 그리기
        ax.scatter(px, py, color=node_color, s=1200, edgecolor=edge_color, linewidth=2, zorder=2)
        # 숫자 텍스트 쓰기
        ax.text(px, py, label, color='white', fontsize=12, fontweight='bold',
                ha='center', va='center', zorder=3)
                
    # 타이틀 및 꾸미기
    ax.set_title(f"Factor Tree of {number} : Decomposing into Prime Atoms", 
                 color='white', fontsize=16, pad=20, fontweight='bold')
    
    # 범례 및 설명 추가
    ax.scatter([], [], color='#0B79D0', s=200, label='Composite Number (Molecule)')
    ax.scatter([], [], color='#2FA85D', s=200, label='Prime Number (Atom)')
    legend = ax.legend(loc='upper right', facecolor='#161B22', edgecolor='#30363D', labelcolor='white')
    
    # 화면 영역 확장 설정
    all_xs = [p[0] for p in points]
    all_ys = [p[1] for p in points]
    ax.set_xlim(min(all_xs) - 1.0, max(all_xs) + 1.0)
    ax.set_ylim(min(all_ys) - 0.5, max(all_ys) + 0.5)
    
    ax.axis('off')
    plt.tight_layout()
    
    output_path = f"01_prime_factorization/factor_tree_{number}.png"
    plt.savefig(output_path, dpi=300, facecolor='#0D1117')
    print(f"소인수분해 트리 시각화가 저장되었습니다: {output_path}")
    plt.show()

if __name__ == "__main__":
    # 테스트로 120 소인수분해 시각화
    plot_factor_tree(120)
