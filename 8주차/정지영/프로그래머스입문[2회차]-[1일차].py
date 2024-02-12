# 1. 개미 군단
def solution(hp):
    
    # 장군개미: 5 / 병정개미: 3 / 일개미: 1
    a = hp // 5
    b = (hp % 5) // 3
    c = ((hp % 5) % 3) // 1
    
    return (a+b+c)

# 2. 모스부호 (1)
def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    ans = ''
    letter_ = letter.split(" ")
    for i in letter_:
        ans += (morse[i])
        
    return ans
        
# 3. 가위 바위 보
def solution(rsp):
    
    winner = {
        '2':'0',  # 가위 < 바위
        '0':'5',  # 바위 < 보
        '5':'2'   # 보 < 가위
    }
    
    ans = ''
    for r in rsp:
        ans += (winner[r])
        
    return (ans)

# 4. 구슬을 나누는 경우의 수
import math
def solution(balls, share):
    
    val = math.factorial(balls) / (math.factorial(share) * math.factorial(balls-share))
    return int(val)

# 5. 점의 위치 구하기
def solution(dot):
    
    if dot[0] > 0 and dot[1] > 0:
        return 1
    
    if dot[0] < 0 and dot[1] > 0:
        return 2
    
    if dot[0] < 0 and dot[1] < 0:
        return 3
    
    if dot[0] > 0 and dot[1] < 0:
        return 4
    
# 6. 2차원으로 만들기
def solution(num_list, n):
    # print(num_list.pop(0))
    # print(num_list)
    
    lst1 = []
    for i in num_list:
        lst1.append(num_list[:n])
        num_list = num_list[n:]
        
        if len(num_list) == 0:
            break
            
    return (lst1)

# 7. 공 던지기
def solution(numbers, k):
    lst = numbers * k
    
    # for i in range(k):
    return (lst[2*(k-1)])

# 8. 배열 회전시키기
def solution(numbers, direction):
    
    if direction == "right":
        ans = [numbers[-1]] + numbers[:-1]
        return ans
        
    else:
        ans = numbers[1:] + [numbers[0]]
        return ans
    
