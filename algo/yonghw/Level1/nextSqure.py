def nextSqure(n):
    j = 1
    while j * j < n:
        j = j + 1
    if j*j == n:
        return (j + 1) * (j + 1)
    else :
        return 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));