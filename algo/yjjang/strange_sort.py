def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    sorted_arr = [strings[0]]
    for i in range(1,len(strings)):
        tmp_str = strings[i]
        for j in range(0, len(sorted_arr)):
            sorted_str = sorted_arr[j]
            if tmp_str[n] < sorted_str[n]:
                sorted_arr.insert(j,tmp_str)
                break
            else:
                if j == len(sorted_arr)-1:
                    sorted_arr.append(tmp_str)
    return sorted_arr

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )