def water_melon(n):
    # 함수를 완성하세요.
    tmp_str = ""
    for n in range(n) :
        if n % 2 == 0 :
            tmp_str = tmp_str + "수"
        else :
            tmp_str = tmp_str + "박"
    return tmp_str


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));