def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    for i in range(strings.__len__()) :
        minindex = i
        for j in range(i, strings.__len__()):
            if ord(strings[minindex][n]) > ord(strings[j][n]):
                minindex = j     
        temp = strings[i]
        strings[i] = strings[minindex]
        strings[minindex] = temp
    return strings


def strange_sort2(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    for i in range(1, strings.__len__()) :
        temp = strings[i]
        j = i
        
        while j > 0 and strings[j - 1][n] > temp[n] :
            strings[j] = strings[j - 1]
            j = j - 1
        strings[j] = temp
    return strings



# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort2(["sun", "bed", "car"], 1) )