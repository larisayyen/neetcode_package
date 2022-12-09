
class EncodeAndDecode:
    '''
    encode a list of strings to a string
    decode the string to the original list
    '''

    def encode(self,list_str):

        res = ""

        for s in list_str:

            # encode s with its length
            res += str(len(s)) + "#" + s

        return res

    def decode(self,str):

        res,i = [],0

        while i < len(str):
            j = i

            # find the word starting with #
            while str[j] != "#":
                j += 1

            length = int(str[i:j])

            # append the word
            res.append(str[j+1 : j+1+length])

            # restart from the end of last word
            i = j + 1 + length

        return res
