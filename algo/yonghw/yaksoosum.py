def sumDivisor(num):
    sum = 0
    
    for i in range(num):
        
        if i != 0 and num % i == 0:
            sum = sum + i

    return sum + num

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumDivisor(12))