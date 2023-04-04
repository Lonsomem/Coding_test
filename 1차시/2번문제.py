global answer
answer = [0,0]
def solution_tree(arr, x, y, size):
    
    if size == 1:
        answer[criteria] += 1
    else:
        for px in range(x, x+size):
            for py in range(y, y+size):
                if arr[px][py] != criteria:
                    solution_tree(arr, x, y, size//2)
                    solution_tree(arr, x+size//2, y, size//2)
                    solution_tree(arr, x, y+size//2, size//2)
                    solution_tree(arr, x+size//2, y+size//2, size//2)
                else:
                    if px == x+size-1 and py == y+size-1:
                        solution_tree(arr, x, y, 1)
                
def solution(arr):
    solution_tree(arr, 0, 0, len(arr))
    return answer

ans = solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
print(ans)