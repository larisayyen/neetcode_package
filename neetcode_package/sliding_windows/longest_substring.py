
def LengthOfLongestSubstring(s):

    # define a unique list of character
    charset = set()

    l = 0
    res = 0

    # iterate index
    for r in range(len(s)):

        # remove character which is repeated
        while s[r] in charset:
            charset.remove(s[l])
            l += 1

        # append character which is unique
        charset.add(s[r])
        res = max(res,r-l+1)

    return res
