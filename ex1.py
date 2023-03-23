def my_func(x1,x2,x3):
    lst= [x1 , x2, x3]
    newLST = []
    Invalid = []
    denominator = None
    counter = None
    for i in lst:
        if type(i)==float:
            newLST.append(i)
        else:
            Invalid.append(i)
    if len(newLST) ==3:
        denominator = (x1 + x2 + x3)
        counter = ((x1+x2+x3)*(x2+x3)*x3)
        if denominator == 0:
            return ("Not a number – denominator equals zero")
        else:
            return (counter/denominator)
    else:
        for X in Invalid:
            if type(X) == int:
                return ("Error: parameters should be float")
            else:
                return ('None')

# print(my_func(1.0,2.0, 3.0))

