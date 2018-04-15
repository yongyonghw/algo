import operator
def sort_dictionary(dic):
    return sorted(dic.items(), key=operator.itemgetter(0))
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( sort_dictionary( {"김철수":78, "기하나":97, "정진원":88} ))