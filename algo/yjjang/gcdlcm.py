def gcdlcm(a, b):
    answer = []
    if a % b == 0 or b % a == 0 :
        if a > b :
            answer = [b, a]
        else :
            answer = [a, b]
    else :
        maxnum = a
        if b > a :
            maxnum = b
        for i in range(maxnum) :
            if i > 0 and a % i == 0 and b % i == 0 :
                answer = [i, (a/i)*(b/i)*i]
                break
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))