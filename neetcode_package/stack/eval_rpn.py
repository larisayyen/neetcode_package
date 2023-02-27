
from typing import List

def evalRPN_s1(tokens: List[str]) -> int:

    '''
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9
    '''
    
    # set a blank list and operator list
    stack = []
    operators = set(["+", "-", "*", "/"])

    for i in tokens:

        if i in operators:
            r = stack.pop()
            l = stack.pop()

            if i == '+':
                res = l + r # no change of order: left first
            elif i == '-':
                res = l - r
            elif i == '*':
                res = l * r
            else:
                res = int(l/r)

            stack.append(res)
        else:
            stack.append(int(i))

    return stack[-1]


def evalRPN_s2(tokens: List[str]) -> int:

    stack=[]
    for ele in tokens:
        if ele in '+-*/':
            a,b=stack.pop(),stack.pop()
        if ele == '+':                
            stack.append(b+a)
        elif ele == '-':                
            stack.append(b-a)
        elif ele == '*':                
            stack.append(b * a)
        elif ele == '/':                
            stack.append(int(b/a))
        else:
            stack.append(int(ele))
            
    return stack[0]  