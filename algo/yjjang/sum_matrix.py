def sumMatrix(A, B):
    answer = []
    n = len(A)
    m = len(A[0])

    for i in range(n):
        tmp_arr = []
        for j in range(m):
            tmp = A[i][j]+B[i][j]
            tmp_arr.append(tmp)
        answer.append(tmp_arr)

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))