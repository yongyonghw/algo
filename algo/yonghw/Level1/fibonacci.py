def fibonacci(num):
    if num <= 1:
        return num
    answer = fibonacci(num - 1) + fibonacci(num - 2)
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))