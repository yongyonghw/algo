def no_continuous(s):
    history = []
    history.append(s[0])
    cnt = s.__len__()
    
    for i in range(cnt):
        if i > 0 and (s[i] != s[i - 1]) :
            print(i)
            history.append(s[i])
    # 함수를 완성하세요
    return history