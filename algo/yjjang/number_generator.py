def number_generator(x, n):
    # 함수를 완성하세요
    tmp_arr = []
    for num in range(n) :
        tmp_arr.append( x * (num+1) )
    return tmp_arr

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(number_generator(3,5))