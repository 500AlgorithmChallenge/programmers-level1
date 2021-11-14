# 문자열 분리 - for문으로 string이 끝날때까지 반복
# 앞 두글자로 판단. if elif ...
# 해당하는 수를 찾으면 정답배열에 숫자 추가
# 그만큼 arr=arr[3: ]
# 이후 반복

s= "2three45sixseven"

def solution(s):
    answer = ""

    while len(s) != 0:
        if s[:2] == "ze":
            answer = answer + '0'
            s = s[4:]
        elif s[:2] == "on":
            answer = answer + '1'
            s = s[3:]
        elif s[:2] == "tw":
            answer = answer + '2'
            s = s[3:]
        elif s[:2] == "th":
            answer = answer + '3'
            s = s[5:]
        elif s[:2] == "fo":
            answer = answer + '4'
            s = s[4:]
        elif s[:2] == "fi":
            answer = answer + '5'
            s = s[4:]
        elif s[:2] == "si":
            answer = answer + '6'
            s = s[3:]
        elif s[:2] == "se":
            answer = answer + '7'
            s = s[5:]
        elif s[:2] == "ei":
            answer = answer + '8'
            s = s[5:]
        elif s[:2] == "ni":
            answer = answer + '9'
            s = s[4:]
        elif s[:1] == "0":
            answer = answer + '0'
            s = s[1:]
        elif s[:1] == "1":
            answer = answer + '1'
            s = s[1:]
        elif s[:1] == "2":
            answer = answer + '2'
            s = s[1:]
        elif s[:1] == "3":
            answer = answer + '3'
            s = s[1:]
        elif s[:1] == "4":
            answer = answer + '4'
            s = s[1:]
        elif s[:1] == "5":
            answer = answer + '5'
            s = s[1:]
        elif s[:1] == "6":
            answer = answer + '6'
            s = s[1:]
        elif s[:1] == "7":
            answer = answer + '7'
            s = s[1:]
        elif s[:1] == "8":
            answer = answer + '8'
            s = s[1:]
        elif s[:1] == "9":
            answer = answer + '9'
            s = s[1:]
        else:
            print('뭔가 이상함')

    return int(answer)

print(solution(s))