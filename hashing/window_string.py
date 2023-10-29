"""
Given a string A and a string B, find the window with minimum length in A which will contain all the characters in B in
linear time complexity.
Note that when the count of a character c in B is x, then the count of c in minimum window in A should be at least x.

Note:
If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index )

Problem Constraints
1 <= size(A), size(B) <= 10^6
"""


# @param A : string
# @param B : string
# @return a strings
def minWindow(A, B):
    len_a, len_b = len(A), len(B)

    b_dict = {}
    for ch in B:
        if ch in b_dict:
            b_dict[ch] += 1
        else:
            b_dict[ch] = 1

    match_count, desired_match_count = 0, len_b
    ans, ans_length = "", float('inf')
    a_dict = {}
    i, j = 0, 0

    while True:

        # acquire
        while i < len_a and match_count < desired_match_count:
            ch = A[i]
            if ch in b_dict:
                if ch in a_dict:
                    a_dict[ch] += 1
                else:
                    a_dict[ch] = 1

                if a_dict[ch] <= b_dict[ch]:
                    match_count += 1
            i += 1

        # release
        while j <= i and match_count == desired_match_count:
            if i - j < ans_length:
                ans, ans_length = A[j:i], i - j
            ch = A[j]
            if ch in a_dict:
                a_dict[ch] -= 1

                if a_dict[ch] < b_dict[ch]:
                    match_count -= 1
            j += 1

        if i == len_a:
            break

    return ans
