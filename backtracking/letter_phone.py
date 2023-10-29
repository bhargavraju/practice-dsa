"""
Given a digit string A, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
The digit 0 maps to 0 itself. The digit 1 maps to 1 itself.

NOTE: Make sure the returned strings are lexicographically sorted.
"""


# @param A : string
# @return a list of strings
def letterCombinations(A):
    mapping = {
        '0': ['0'],
        '1': ['1'],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def rec_helper(s, curr, res):
        if len(s) == 0:
            res.append(curr)
            return

        num = s[0]
        for val in mapping[num]:
            rec_helper(s[1:], curr + val, res)

    ans = []
    rec_helper(A, "", ans)
    ans.sort()
    return ans
