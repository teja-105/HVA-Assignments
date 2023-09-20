def is_balanced_parentheses_array(testVariable, startIndex=0, currentIndex=0):
    a = []
    b = []

    for i in range(startIndex, len(testVariable)):
        if testVariable[i] == "(":
            a.append("(")
        elif testVariable[i] == ")":
            b.append(")")

    if len(a)==len(b):
        return True
    else:
        return False

parentheses_input = input("Enter a sequence of parentheses: ")
parentheses_array = list(parentheses_input)


is_balanced_parentheses_array(parentheses_array)

if  is_balanced_parentheses_array(parentheses_array):
    print("The brackets are balanced.")
else : 
    print("The brackets are not balanced.")