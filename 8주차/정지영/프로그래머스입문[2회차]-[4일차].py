# 1. 영어가 싫어요

def solution(numbers):
    
    dict = {
        'zero':0,
        'one':1, 
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8, 
        'nine':9
           }
    
    for k, v in dict.items():
        numbers = (numbers.replace(k, str(v)))
        
    return int(numbers)
            
# 2. 인덱스 바꾸기

def solution(my_string, num1, num2):
    
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    ans = ''.join(my_string)
    
    return (ans)
    
# 3. 한 번만 등장한 문자

def solution(s):
    
    c = {}
    for i in s:
        if i not in c:
            c[i] = 1
        
        else:
            c[i] += 1
            
    aa = ''
    for k, v in c.items():
        if v == 1:
            aa += k
            
    return (''.join(sorted(aa)))

# 4. 약수 구하기

def solution(n):
    
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
            
    return sorted(lst)

# 5. 편지

def solution(message):

    return (len(message)*2)

# 6. 가장 큰 수 찾기

def solution(array):
    
    lst = []
    
    max_val = max(array)
    max_index = array.index(max_val)
    
    lst.append(max_val)
    lst.append(max_index)
    
    return lst

# 7. 문자열 계산하기 (🐼 python 내장 함수 eval)

def solution(my_string):
    
    # print(eval(my_string)) 
    
    split_str = my_string.split()
    ans = int(split_str[0])
    
    
    for i in range(len(split_str)):
        if split_str[i] == '+':
            ans += int(split_str[i+1])
        
        elif split_str[i] == '-':
            ans -= int(split_str[i+1]) 
            
    return (ans)

# 8. 배열의 유사도

def solution(s1, s2):
    
    cnt = 0
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            
            if s1[i] == s2[j]:
                cnt += 1
                
    return (cnt)