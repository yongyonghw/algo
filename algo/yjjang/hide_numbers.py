def hide_numbers(s):
    #함수를 완성해 별이를 도와주세요
    str_len = len(s)
    tmp_str = ""
    if str_len < 4 :
        return s
    else :
        for i in range(str_len-4) :
        	tmp_str = tmp_str + "*"
        tmp_str = tmp_str + s[str_len-4:str_len]
    return tmp_str

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));