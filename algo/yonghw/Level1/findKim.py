def findKim(seoul):
    # 함수를 완성하세요
    for i in range(seoul.__len__()):
        if seoul[i] == "Kim":
            return "김서방은 {}에 있다".format(i)


# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))

