def sumMatrix(A,B):
    
    x = A.__len__()
    y = A[0].__len__()
    
    for i in range(x): 
        for j in range(y):
            A[i][j] += B[i][j]
    
    return A

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))