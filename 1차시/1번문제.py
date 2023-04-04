N = int(input())

table = [[0 for i in range(1, N+1)] for g in range(1, N+1)] # N*N 배열

print(table)
num = 1
x = -1 #내려가면서 시작하기 때문에 -1
y = 0

for f in range(1, N+1):
    for _ in range(0, N-f+1):   # 진행상황
        if f % 3 == 1: #높이
            x += 1
            print('높이')
        elif f % 3 == 2: #밑변
            y += 1
            print('밑변')
        else:          #빗변
            x -= 1
            y -= 1
            print('빗변')
        table[x][y] = num
        num += 1
        print(x, y, num)
print(table) 


