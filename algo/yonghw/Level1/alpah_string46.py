def alpha_string46(s):
    # 함수를 완성하세요
    if isNumber and (s.__len__() == 4 or s.__len__() == 6):
        return True
    else :
        return False

    
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
