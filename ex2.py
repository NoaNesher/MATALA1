def revword(word:str):
    return word.lower()[::-1]
def countword(th):
    lst = []
    for line in th:
        lst.append(line.rstrip().split())
    WORD = lst[0][0]
    checklist = []
    count = 1
    for i in lst[1:]:
        for X in i:
            checklist.append(revword(X))
    for word in checklist:
        if word == WORD:
            count = count + 1
    return (count)

# th = open("C:/mypython/MATALA1/text.txt")
# print(countword(th))