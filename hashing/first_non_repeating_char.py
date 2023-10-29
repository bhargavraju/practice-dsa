"""
Given a string A denoting a stream of lowercase alphabets. You have to make new string B.
B is formed such that we have to find first non-repeating character each time a character is inserted to the stream
and append it at the end to B. if no non-repeating character is found then append '#' at the end of B.

Problem Constraints
1 <= |A| <= 100000

Example:
    input: A = "abadbc"
    output: "aaabc#"
    Explanation:
    "a"      -   first non repeating character 'a'
    "ab"     -   first non repeating character 'a'
    "abc"    -   first non repeating character 'a'
    "abca"   -   first non repeating character 'b'
    "abcab"  -   first non repeating character 'c'
    "abcabc" -   no non repeating character so '#'
"""


# @param A : string
# @return a strings
def solve(A):
    n = len(A)
    char_map = {}
    ans = ""
    j = 0
    for i in range(n):
        if A[i] in char_map:
            char_map[A[i]] += 1
        else:
            char_map[A[i]] = 1

        if char_map[A[j]] > 1:
            while j <= i:
                if char_map[A[j]] > 1:
                    j += 1
                else:
                    break

        ans += "#" if j == i + 1 else A[j]

    return ans
