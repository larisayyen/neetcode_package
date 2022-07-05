
def isvalid(s):

    # define dict and list
    pair = {')' : '(' ,
            ']' : '[' ,
            '}' : '{'}

    open = set('([{')
    close = set(')]}')

    list_of_s = []


    for i in s:

        # add opening parentheses into list
        if i in open:
            list_of_s.append(i)

        # match the closing with opening
        if i in close:
            if not list_of_s:
                return False

            # pop out the opening when there is a match
            elif list_of_s.pop() != pair[i]:
                return False
            else:
                continue

    # nothing left in the list, return True
    if not list_of_s:
        return True
    else:
        return False

def generate(n):

    stack = []
    res = []

    def backtrack(open,close):
        if open == close == n:
            res.append(''.join(stack))
            return

        # add an opening parenthese
        if open < n:
            stack.append('(')
            backtrack(open+1,close)
            stack.pop()

        # add a closing parenthese
        if open > close:
            stack.append(')')
            backtrack(open,close+1)
            stack.pop()

    backtrack(0,0)
    return res
