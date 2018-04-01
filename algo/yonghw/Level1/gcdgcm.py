
def gcd(m, n):
    r = 0
    while True:
        r = m % n
        if r == 0:
            return n
        else:
            m = n
            n = r;
def gcm(m, n):
    return m * n / gcd(m, n);

def gcdlcm(a, b):
    answer = []
    answer.append(gcd(a,b))
    answer.append(gcm(a,b))
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3, 12))
