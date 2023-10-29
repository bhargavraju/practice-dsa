"""
Given a string A, partition A such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of A.

Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
(len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))

Input 1:
A = "aab"

Output 1:
 [
    ["a","a","b"]
    ["aa","b"],
  ]
"""


# @param A : string
# @return a list of list of strings
def partition(A):
    n = len(A)

    def is_palindrome(s):
        if len(s) < 2:
            return True
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def rec_helper(i, curr, res):
        if i == n:
            res.append(curr)
            return
        j = i + 1
        while j <= n:
            sub_str = A[i:j]
            if is_palindrome(sub_str):
                rec_helper(j, curr + [sub_str], res)
            j += 1

    ans = []
    rec_helper(0, [], ans)
    return ans
