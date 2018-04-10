def string_middle(str):
    # 함수를 완성하세요
    length = str.__len__()
    result = "";

    if length % 2 == 0:
        index = length / 2 - 1
        result = str[int( length/2 -1 )] + str[int (length/2)]
    else :
        result = str[int (length/2)]

    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("powerg"))