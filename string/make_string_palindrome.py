"""
Given a string A of size N consisting only of lowercase alphabets. The only operation allowed is to insert characters
in the beginning of the string. Find and return how many minimum characters are needed to be inserted to make
the string a palindrome string.
"""


# @param A : string
# @return an integer
def solve(A):
    n = len(A)
    test_str = A + '$' + A[::-1]
    lps = [0] * (2 * n + 1)

    def build_lps():
        i, j = 0, 1
        while j < 2 * n + 1:
            if test_str[i] == test_str[j]:
                lps[j] = i + 1
                i += 1
                j += 1
            else:
                if i != 0:
                    i = lps[i - 1]
                else:
                    lps[j] = 0
                    j += 1

    build_lps()
    return n - lps[-1]
