# 1. 모음 제거
def solution(my_string):
    word = ['a','e','i','o','u']
    
    ans = ''
    for m in my_string:
        if m not in word:
            ans += m
            
    return (ans)

# 2. 문자열 정렬하기 (1)
def solution(my_string):
    
    lst = []
    for m in my_string:
        if m.isdigit():
            lst.append(int(m))
            
    lst = sorted(lst)
    return (lst)


# 3. 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    
    ans = 0
    
    for i in my_string:
        if i.isdigit():
            ans += int(i)
            
    return (ans)

# 4. 소인수분해
def solution(n):
    
    ans = []
    d = 2
    while d <= n:
        if n % d == 0:
            ans.append(d)
            n = n / d
        
        else:
            d = d + 1
            
    return (sorted(list(set(ans))))

# 5. 컨트롤 제트
def solution(s):
    
    ans = []
    for i in s.split(" "):
        if i != "Z":
            ans.append(int(i))
            
        elif i == 'Z':
            ans.pop(-1)
            
    return (sum(ans))

# 6. 배열 원소의 길이
def solution(strlist):
    
    ans = []
    for i in strlist:
        ans.append(len(i))
        
    return (ans)

# 7. 중복된 문자 제거
def solution(my_string):
    
    ans = []
    for i in my_string:
        
        if i not in ans:
            ans.append(i)
            
    return (''.join(ans))        

# 8. 삼각형의 완성조건 (1)
def solution(sides):
    
    val = sorted(sides)
    max_val = val[-1]
    not_max_val = val[:-1]
    
    if max_val >= sum(not_max_val):
        return 2
    else:
        return 1