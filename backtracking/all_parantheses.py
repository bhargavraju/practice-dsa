"""
Given an integer A pairs of parentheses,
write a function to generate all combinations of well-formed parentheses of length 2*A.
"""


# @param A : integer
# @return a list of strings
def generateParenthesis(A):
    ans = []

    def rec_helper(left, right, curr, res):
        if left > A or right > A:
            return
        if left == right == A:
            res.append(curr)
            return

        if left < A:
            rec_helper(left + 1, right, curr + "(", res)
        if right < left:
            rec_helper(left, right + 1, curr + ")", res)

    rec_helper(0, 0, "", ans)
    return ans
