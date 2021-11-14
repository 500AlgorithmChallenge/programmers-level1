def solution(numbers):
    answer = -1
    li=[] #없는 숫자 담을 배열
    for i in range(0,10):
        if i not in numbers: #numbers배열에 없는 숫자이면!
             li.append(i) #li에 숫자를 다 담는다
    answer=sum(li) #그 숫자를 다 더한다
    return answer