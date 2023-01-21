
def lengthOfLongestSubstring(s):
    '''
    return the length of the longest substring without repeating chars
    '''
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res,r-l+1)

    return res

def characterReplacement(s,k):
    '''
    given a string and replace some characters k times
    to return the length of repeating letters
    '''
    # windowlength - count(most_repeated_character)

    count = {}
    res = 0

    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r],0)
        maxf = max(maxf,count[s[r]])

        if (r-l+1) -maxf >k:
            count[s[l]] -= 1
            l += 1

        res = max(res,r-l+1)

    return res
