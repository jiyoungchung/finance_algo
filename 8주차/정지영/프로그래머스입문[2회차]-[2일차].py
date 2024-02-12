# 1. 주사위의 개수
def solution(box, n):
    
    return (box[0]//n) * (box[1]//n) * (box[2]//n)

# 2. 합성수 찾기
def solution(n):
    ans = 0
    for i in range(1, n+1):
        
        cnt = 0
        
        for j in range(1, i+1):
            
            if i % j == 0:
                cnt += 1
        
        if cnt >= 3:
            ans += 1
            
    return (ans)

# 3. 최댓값 만들기(1)
from itertools import combinations

def solution(numbers):
    
    ans = []
    
    for i in combinations(numbers, 2):
        val = i[0] * i[1]
        ans.append(val)
        
    return (max(ans))

# 4. 팩토리얼
import math

def solution(n):
    
    k = 10
    while n < math.factorial(k):
        k -= 1
    
    return k
