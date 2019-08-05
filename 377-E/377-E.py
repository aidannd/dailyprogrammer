# https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/

def fit1(X, Y, x, y):
    return int(X/x)*int(Y/y)
 
assert fit1(25, 18, 6, 5) == 12
assert fit1(10, 10, 1, 1) == 100
assert fit1(12, 34, 5, 6) == 10
assert fit1(12345, 678910, 1112, 1314) == 5676
assert fit1(5, 100, 6, 1) == 0

def fit2(X, Y, x, y):
    beforeTurn = int(X/x)*int(Y/y)
    afterTurn = int(X/y)*int(Y/x)
    if beforeTurn > afterTurn:
        return beforeTurn
    else:
        return afterTurn

assert fit2(25, 18, 6, 5) == 15
assert fit2(12, 34, 5, 6) == 12
assert fit2(12345, 678910, 1112, 1314) == 5676
assert fit2(5, 5, 3, 2) == 2
assert fit2(5, 100, 6, 1) == 80
assert fit2(5, 5, 6, 1) == 0

def fit3(X, Y, Z, x, y, z):
    calculations = []
    calculations.append(int(X/x)*int(Y/y)*int(Z/z))
    calculations.append(int(X/x)*int(Y/z)*int(Z/y))
    calculations.append(int(X/y)*int(Y/z)*int(Z/x))
    calculations.append(int(X/y)*int(Y/x)*int(Z/z))
    calculations.append(int(X/z)*int(Y/x)*int(Z/y))
    calculations.append(int(X/z)*int(Y/y)*int(Z/x))

    return max(calculations)

assert fit3(10, 10, 10, 1, 1, 1) == 1000
assert fit3(12, 34, 56, 7, 8, 9) == 32
assert fit3(123, 456, 789, 10, 11, 12) == 32604
assert fit3(1234567, 89101112, 13141516, 171819, 202122, 232425) == 174648

def fitn(crate, box):
     pass