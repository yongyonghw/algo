import math
def nextSqure(n):
    # 함수를 완성하세요
    num = math.sqrt(n)
    if num % 1 == 0:
        return (int(num) + 1) * (int(num) + 1)
    return 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));
