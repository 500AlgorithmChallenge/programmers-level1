def solution(absolutes, signs):
    answer = 123456789
    num=[]
    result=0
    for i in range(len(absolutes)):
        if signs[i]==1:
            num.append(absolutes[i])
        else:
            num.append(-absolutes[i])
    answer=sum(num)
    return answer