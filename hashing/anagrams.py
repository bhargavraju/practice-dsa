"""
Given an array A of N strings, return all groups of strings that are anagrams. Represent a group by a list of integers
representing the index(1-based) in the original list.

NOTE: Anagram: a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'.

Problem Constraints
1 <= N <= 10^4
1 <= |A[i]| <= 10^4

Each string consists only of lowercase characters.
Sum of length of all the strings doesn't exceed 10^7

Input 1:
A = [cat, dog, god, tca]
Output 1:
[ [1, 4],
[2, 3] ]
"""


# @param A : tuple of strings
# @return a list of list of integers
def anagrams(A):
    n = len(A)

    def string_to_dict(s):
        char_dict = {}
        for ch in s:
            if ch in char_dict:
                char_dict[ch] += 1
            else:
                char_dict[ch] = 1
        return char_dict

    visited = [0] * n
    ans = []
    for i in range(n):
        if visited[i] == 1:
            continue
        else:
            visited[i] = 1

        char_map = string_to_dict(A[i])
        group = [i + 1]

        for j in range(i + 1, n):
            if visited[j] == 1:
                continue
            if string_to_dict(A[j]) == char_map:
                group.append(j + 1)
                visited[j] = 1

        ans.append(group)

    return ans
