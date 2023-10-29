"""
Given a string A consisting of lowercase English alphabets. Find and return lexicographically smallest string B after
removing duplicate letters from A so that every letter appears once and only once. The order of the alphabets in the
original string should be preserved.

Input Format:
The only argument given is string A.

Output Format:
Return lexicographically smallest string B after removing duplicate letters from A.

Constraints:
1 <= length of the string <= 200000
A consists of lowercase English alphabets only.

For Example
Input 1:
    A = "cbacdcbc"
Output 1:
    B = "acdb"

Input 2:
    A = "bcabc"
Output 2:
    B = "abc"
"""


# @param A : string
# @return a strings
def solve(A):
    char_count = {}
    visited = set()
    stack = []
    for ch in A:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

    for ch in A:
        char_count[ch] -= 1
        if ch in visited:
            continue
        while len(stack) > 0 and stack[-1] > ch:
            if char_count[stack[-1]] > 0:
                popped = stack.pop()
                visited.remove(popped)
            else:
                break
        stack.append(ch)
        visited.add(ch)

    return "".join(stack)
