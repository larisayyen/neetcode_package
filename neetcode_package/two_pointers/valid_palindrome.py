
def isPalindrome_s1(s):
    '''
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
    '''

    newstr = ''

    for c in s:
        if c.isalnum():
            newstr += c.lower()

    return newstr == newstr[::-1]

def isPalindrome_s2(s):
    '''
    solution without creating a new string
    '''
    l,r = 0,len(s) - 1

    while l < r:

        while l < r and not alphaNum(s[l]):
            l += 1
        while r > 1 and not alphaNum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l,r = l+1,r-1
    return True

def alphaNum(c):
    '''
    ascii value of a character : ord()
    '''
    return (
        ord('A') <= ord(c) <= ord('Z') # upper case
        or ord('a') <= ord(c) <= ord('z') # lower case
        or ord('0') <= ord(c) <= ord('9') # numeric
    )

def isPalindrome_s3(s):

    left = 0
    right = len(s)-1
    while left < right:
        # Step 1
        while left < right and not s[left].isalnum():
            left += 1
        #Step 2
        while left < right and not s[right].isalnum():
            right -= 1
        # Steps 3 and 4
        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    # Step 6
    return True
