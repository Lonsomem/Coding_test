# 소수점 버리기 : 그냥 int() 씌우면 버림
# 문자열.lower()

def solution(str1, str2):
    answer = 0
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    str1list = []
    str2list = []

    for i in range(len(str1)-1):
        if str1[i] in letter and str1[i+1] in letter:
            strset = str1[i].lower() + str1[i+1].lower()
            str1list.append(strset)
        else:
            continue
            
    for i in range(len(str2)-1):
        if str2[i] in letter and str2[i+1] in letter:
            strset = str2[i].lower() + str2[i+1].lower()
            str2list.append(strset)
        else:
            continue
    
    for 
    

    return answer