def average(array):
    sum = 0
    
    for i in range(array.__len__()):
        sum += array[i]
    
    # 함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
    return sum / array.__len__()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)));