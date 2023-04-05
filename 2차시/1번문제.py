# https://school.programmers.co.kr/learn/courses/30/lessons/64061

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