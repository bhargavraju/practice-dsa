"""
You are given a string A. An operation on the string is defined as follows:
Remove the first occurrence of same consecutive characters. eg for a string "abbcd", the first occurrence of same
consecutive characters is "bb". Therefore the string after this operation will be "acd".

Keep performing this operation on the string until there are no more occurrences of same consecutive characters and
return the final string.
"""


# @param A : string
# @return a strings
def solve(A):
    chars = []
    for el in A:
        if len(chars) > 0 and chars[-1] == el:
            chars.pop()
        else:
            chars.append(el)
    return "".join(chars)
