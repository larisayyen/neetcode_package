
def ispalindrome(str):

    # convert a sentence into sequence
    seq = ''
    for i in str:
        if i.isalpha():
            seq += i
        elif i.isdigit():
            seq += i

    # convert into lowercase
    seq = seq.lower()

    # compare the two halves of sequence
    for i in range(len(seq)//2):
        if seq[i] != seq[len(seq)-1-i]:
            return False

    return True
