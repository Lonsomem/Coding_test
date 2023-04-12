#https://school.programmers.co.kr/learn/courses/30/lessons/64064

def solution(user_id, banned_id):
    answer = 1
    check = False
    for bid in banned_id:
        count = 0
        cid = [pos for pos, char in enumerate(bid) if char != '*']
        for uid in user_id:
            for c in cid:
                if len(uid) != len(bid) or uid[c] != bid[c]:
                    check = True
                    break
            if check == False:
                count += 1
            check = False
        answer *= count

    return answer

res = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
print(res)
