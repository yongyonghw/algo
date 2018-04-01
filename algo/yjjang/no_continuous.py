def no_continuous(s):
    # 함수를 완성하세요
    tmp_arr = []
    tmp_str = ""
    for n in range(len(s)) :
        if tmp_str != s[n] :
            tmp_str = s[n]
            tmp_arr.append(s[n])
    return tmp_arr

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
print( no_continuous( "47330" ))