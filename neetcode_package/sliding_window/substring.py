
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

        if (r-l+1) -maxf >k: # windowlength :r-l+1
            count[s[l]] -= 1
            l += 1

        res = max(res,r-l+1)

    return res

def checkInclusion(s1,s2):
    '''
    check if s1 is a substring of s2
    '''
    if len(s1) > len(s2):
        return False

    s1count,s2count = [0]*26,[0]*26

    for i in range(len(s1)):
        s1count[ord(s1[i]) - ord('a')] += 1
        s2count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1count[i] == s2count[i] else 0)

    l = 0
    for r in range(len(s1),len(s2)):

        if matches == 26:
            return True

        index = ord(s2[r]) - ord('a')
        s2count[index] += 1

        if s1count[index] == s2count[index]:
            matches += 1
        elif s1count[index] + 1 == s2count[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2count[index] -= 1

        if s1count[index] == s2count[index]:
            matches += 1
        elif s1count[index] + 1 == s2count[index]:
            matches -= 1

        l += 1

    return matches == 26

# def get_permutation(string, i=0):

#     if i == len(string):
#         print("".join(string))

#     for j in range(i, len(string)):

#         words = [c for c in string]

#         # swap
#         words[i], words[j] = words[j], words[i]

#         get_permutation(words, i + 1)

# print(get_permutation('yup'))

def minWindow(s,t):

    if t == "":
        return ""

    countT,window = {},{}

    for c in t:
        countT[c] = 1 + countT.get(c,0)

    have,need = 0,len(countT)
    res ,resLen = [-1,-1],float('infinity')
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c,0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:

            # update our result
            if (r - l + 1) < resLen:
                 res = [l,r]
                 resLen = (r - l + 1)

            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1

            l += 1

    l,r = res
    return s[l:r+1] if resLen != float('infinity') else ""


import collections

def maxSlidingWindow(nums, k):
    '''
    return the maximum of every window
    '''
    output = []

    l = r = 0

    q = collections.deque()

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()

        q.append(r)

        # remove left value from window

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1

        r += 1
        return output
