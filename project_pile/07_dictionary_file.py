def sort_freq(filename):
    '''
    결과로 글자의 총 갯수와, 등장한 글자의 종류, 그리고 각 횟수를 보여준다.

    (T:5), (h:10), .... << 각 횟수
    글자의 총 갯수 : 1번째 값의 총합
    글자의 종류 : ()의 갯수
    '''
    infile = open(filename, "r")
    dic = {}
    dica = dic.copy()
    
    i = 0
    j = 0
    for line in infile:
        line = line.rstrip()
        for word_line in line:
            for dan in word_line:
                if dan in dica.keys():
                    dica[dan] += 1
                else:
                    dica[dan] = 1
        
    for word in dica.keys():
        i += 1
    print("글자의 종류: ",i)
    for word in dica.values():
        j += word
    print("글자의 총 갯수", j)
    
    infile.close()
    return dica

                    



print(sort_freq("news.txt"))