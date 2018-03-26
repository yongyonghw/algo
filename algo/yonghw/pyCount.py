def numPY(s):
    pCnt = 0
    yCnt = 0
    for i in range(s.__len__()) :
        j = s[i]
        if j == 'p' or j == 'P':
            pCnt = pCnt + 1
        elif j == 'y' or j == 'Y':
            yCnt = yCnt + 1
    if pCnt != yCnt:
        return False
    else:
        return True 