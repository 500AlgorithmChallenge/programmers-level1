# absolutes 1 이상 1000 이하
# sign - true면 양, false면 음
# absolute

def (absolutes, sign) :
    for i in len(absolutes):
        if sign[i] == true:
            continue
        elif sign[i] == false:
            absolute = -absolute[i]

    for i in absolute:
        answer += i

    return answer