# https://school.programmers.co.kr/learn/courses/30/lessons/64061
'''
def solution(board, move):
    answer = 0
    basket = []
    board1 = [[] for _ in range(len(board))]
    for col in range(len(board)):               # board 역으로 정렬
        for element_id in range(len(board)):
            if board[col][element_id] != 0:
                board1[element_id].insert(0, board[col][element_id])
            else:
                continue                         
    for c in move:                               # 움직임 순번; 인덱스+1;
        if board1[c-1] != []:                     # board 비어있지 않을 때
            if basket != []:                     # 바구니가 비어있지 않을 때
                if board1[c-1][-1] == basket[-1]: # 바구니랑 뽑은 인형 같을 떄
                    basket.pop()
                    answer += 2
                else:                            # 바구니랑 뽑은 인형 다를 때
                    basket.append(board1[c-1][-1])
                    board1[c-1].pop()
            else:                                # 바구니 비어있을 때
                basket.append(board1[c-1][-1])
                board1[c-1].pop()
        else:                                    # board 비어있을 때
            continue
    return answer
    '''

def solution(board, move):
    
    answer = 0
    depth = 0
    basket = []
    
    for count in range(len(move)):
        while depth < len(board) and board[depth][move[count]-1] == 0 :
            depth += 1
        if depth < len(board):
            if basket != []:
                if basket[-1] == board[depth][move[count]-1]:
                    answer += 2
                    board[depth][move[count]-1] = 0
                    basket.pop()
                else:
                    basket.append(board[depth][move[count]-1])
                    board[depth][move[count]-1] = 0
            else:
                basket.append(board[depth][move[count]-1])
                board[depth][move[count]-1] = 0
        
            depth = 0
        else:
            depth = 0

    return answer 

res = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(res)