
def isHappy(n):

    visit = set() # O(n)

    while n not in visit:
        visit.add(n)

        n = sumOfSquare(n)

        if n == 1:
            return True
        return False


    def sumOfSquare(number):
        '''
        19 % 10 = 9
        19 // 10 = 1
        1 % 10 = 0
        1 // 10 = 0
        '''
        output = 0

        while n:
            digit = n % 10
            digit = digit **2
            output += digit

            n = n // 10

        return output

def plusOne(digits):

    one , i = 1,0
    digits = digits[::-1] # 2,3,4 -> 4,3,2

    while one:
        if i < len(digits):

            if digits[i] == 9:
                digits[i] = 0

            else:
                digits[i] += 1 # 4,3,2 -> 5,3,2
                one = 0 # stop the while loop and return output
        else:
            digits.append(one)
            one = 0

        i += 1

        return digits[::-1] # 5,3,2 -> 2,3,5
