import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    """주어진 정수가 소수인지 판별하는 함수"""
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def create_ulam_spiral(size):
    """size x size 크기의 울람 나선 행렬을 생성하는 함수"""
    # 홀수 크기로 보정
    if size % 2 == 0:
        size += 1
        
    grid = np.zeros((size, size), dtype=int)
    
    # 나선형 이동 방향 벡터 (우, 상, 좌, 하)
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    # 시작점 (중앙)
    x, y = size // 2, size // 2
    grid[y, x] = 1
    
    step_limit = 1  # 현재 방향으로 나아갈 칸 수
    step_count = 0  # 현재 방향으로 나아간 칸 수
    dir_idx = 0     # 현재 방향 인덱스
    change_count = 0 # 방향을 꺾은 횟수 (2번 꺾을 때마다 step_limit이 1씩 증가)
    
    for val in range(2, size * size + 1):
        # 이동
        x += dx[dir_idx]
        y += dy[dir_idx]
        grid[y, x] = val
        
        step_count += 1
        if step_count == step_limit:
            step_count = 0
            dir_idx = (dir_idx + 1) % 4
            change_count += 1
            if change_count == 2:
                change_count = 0
                step_limit += 1
                
    return grid

def plot_ulam_spiral(size=150):
    """울람 나선을 시각화하는 함수"""
    print(f"[{size}x{size}] 크기의 울람 나선 격자를 생성 중입니다...")
    grid = create_ulam_spiral(size)
    
    # 각 격자점이 소수인지 여부를 판별하여 이진 행렬 생성
    prime_mask = np.vectorize(is_prime)(grid)
    
    plt.figure(figsize=(10, 10), facecolor='#0D1117')  # Premium Dark Theme
    ax = plt.subplot(111)
    ax.set_facecolor('#0D1117')
    
    # 소수 위치에 점 찍기
    y_indices, x_indices = np.where(prime_mask)
    ax.scatter(x_indices, y_indices, color='#2FA85D', s=2, alpha=0.8, label='Prime Numbers')
    
    # 중앙 시작점(1) 하이라이트
    ax.scatter(size//2, size//2, color='#0B79D0', s=30, edgecolor='white', zorder=5, label='Center (1)')
    
    # 디자인 디테일 설정
    ax.set_title("Ulam Spiral: The Architecture of Primes", color='white', fontsize=16, pad=20, fontweight='bold')
    ax.text(0.5, -0.05, "Every dot represents a prime number. Notice the mysterious diagonal lines (patterns).", 
            color='#8B949E', fontsize=10, ha='center', transform=ax.transAxes)
            
    ax.axis('off')
    plt.tight_layout()
    
    # 이미지로 저장 및 출력
    output_path = "01_prime_factorization/ulam_spiral.png"
    plt.savefig(output_path, dpi=300, facecolor='#0D1117')
    print(f"시각화 이미지가 성공적으로 저장되었습니다: {output_path}")
    plt.show()

if __name__ == "__main__":
    plot_ulam_spiral(201)
