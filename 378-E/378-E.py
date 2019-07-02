'''
Implementation of the Havel-Hakimi algorithm
'''
boolOutputs = []


def hh(input):
    """
    Takes in an input list
    Returns True if the list is consistent and it's possible everyone is telling the truth
    Returns False if the answers are inconsistent
    """
    #1
    for num in input:
        if num == 0:
            input.remove(num)
            return(hh(input))
    #2
    if len(input) == 0:
        boolOutputs.append("true")
        return True
    #3
    input.sort(reverse=True)
    #4
    largestNum = input[0]
    input.remove(largestNum)
    #5
    if largestNum > len(input):
        boolOutputs.append("false")
        return False
    #6
    for i in range(largestNum):
        input[i] -= 1
    return(hh(input))

# Reads test cases and turns each line into a list of integers and feeds it into the hh algorithm
tests = open("testcases.txt")
for line in tests:
    testlist = list((line.strip()).split(","))
    testlist = list(map(int, testlist))
    hh(testlist)
hh([]) # "[]" test case, couldn't read normally

# Read correct answers from text file and compare to calculated answers
answers = open("answers.txt")
linenum = 0
for line in answers:
    if not boolOutputs[linenum] == (line.strip()):
        print("Test case ", linenum+1, " is wrong")
    else:
        print("Test case ", linenum+1, " is right")
    linenum +=1