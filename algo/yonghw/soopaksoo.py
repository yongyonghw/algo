def water_melon(n):
    str = ""
    for i in range(n):
        if i % 2 and n > 0 == 0:
            str += '박'
        else:
            str += '수'
    # 함수를 완성하세요.
    return str


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
