# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, move):
    basket = []                                  # 바구니

    for c in move:                               # 움직임 순번; 인덱스+1;
        if board[c-1][-1] == 0:
            while 0 not in board[c-1]:       # 0인 인형 없을 때까지
        
        
        if basket != []:                     # 바구니가 비어있지 않을 때
            if board[c-1][-1] == basket[-1]: # 바구니랑 뽑은 인형 같을 떄
                basket.pop()
            else:                            # 바구니랑 뽑은 인형 다를 때
                basket.append(board[c-1][-1])
                board[c-1].pop()
        else:                                # 바구니 비어있을 때
            basket.apend(board[c-1][-1])


                

        
        
        







    answer = 0
    return answer