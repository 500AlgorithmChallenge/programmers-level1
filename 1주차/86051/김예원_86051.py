# 엎는 수 찾아 더하기
# numbers는 0~9까지
# numbers를 오름차순 정렬
# while :
# j += 1
# 반복문으로 찾기.
# for i in numbers:
#   if i == j: break
# answer += j

numbers = [5,8,4,0,6,7,9]

def solution(numbers):
    answer = 0
    sn = sorted(numbers)

    i=0
    for j in sn:
        if j != i:
            while i < j:
                answer += i
                i += 1
        i += 1

    if sn[len(sn)-1] != 9:
        while i < 10:
            answer += i
            i+=1


    return answer

print(solution(numbers))