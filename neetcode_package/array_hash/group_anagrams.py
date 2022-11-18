
from itertools import groupby
from collections import defaultdict

def GroupAnagram_s1(strs_list):
    '''
    given a list of strings
    categorize same strings into groups
    s1 uses basic dictionary solution
    '''

    test = defaultdict(list)

    for i in strs_list:
        k = sorted(i)
        k_ = ''.join(n for n in k)
        # print(k_)
        test[k_].append(i)

    result = list(test.values())

    return result

strs_list = ['eat','tea','kil','lik']
GroupAnagram_s1(strs_list)

def GroupAnagram_s2(strs_list):
    '''
    s2 uses charCount solution
    '''
    res = defaultdict(list)

    for s in strs_list:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)
        # tuple(count) be like (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)

    return res.values()

strs_list = ['eat','tea','kil','lik']
GroupAnagram_s2(strs_list)

def GroupAnagram_s3(strs_list):
    '''
    s3 uses lambda and groupby solution
    '''
    temp = lambda strs_list : sorted(strs_list)
    print(temp)

    res = [list(val) for key, val in groupby(sorted(strs_list, key = temp), temp)]
    print(res)

    return res


strs_list = ['eat','tea','kil','lik']
GroupAnagram_s3(strs_list)
