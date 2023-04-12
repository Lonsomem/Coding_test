#https://school.programmers.co.kr/learn/courses/30/lessons/68936

global answer
answer = [0,0]

def quad_tree(arr, x, y, size):
    check = True
    for px in range(x, x+size//2):
        for py in range(y, y+size//2):
            if arr[px][py] != arr[x][y]:
                check = False
    if check == False:
        quad_tree(arr, x, y, size//2)
        quad_tree(arr, x+size//2, y, size//2)
        quad_tree(arr, x, y+size//2, size//2)
        quad_tree(arr, x+size//2, y+size//2, size//2)
    else:
        answer[arr[x][y]] += 1


res = quad_tree([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]], 0, 0, len([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(res)