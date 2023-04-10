s = input()

c0 = 0 # 0의 갯수
c1 = 0 # 실행한 횟수
while s != '1': 
    c0 += s.count('0')    
    c1 += 1
    s = s.replace('0','')
    s = str(bin(len(s))) 
    s = s[2::] # bin() 을 문자열로 바꾸면 0bxx 가 됨, 0b 뒤의 수를 가져올 수 있도록 함
print([c1, c0])