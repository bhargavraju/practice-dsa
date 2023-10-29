"""
Given a string A of size N, consider all duplicated substrings: (contiguous) substrings of A that occur 2 or more
times. (The occurrences may overlap.) Return the longest possible length of the duplicated substring.

NOTE: If A does not have a duplicated substring, return 0.

Problem Constraints
2 <= N <= 10^5

A consists of lowercase English letters.

Input Format
Only argument is a string A of size N.

Output Format
Return a string denoting a duplicated substring that has the longest possible length.

Solution Explanation:
If duplicates exist for length k, duplicates will exist for all lengths less than k. Which means, if we don't find
duplicates for a particular length, we can ignore all lengths greater than that.

To check for duplicates, used Rabin-karp algorithm which uses rolling hash to compare substrings
"""


# @param A : string
# @return an integer
def solve(A):
    n = len(A)
    d = 256
    q = 1000000007

    def duplicate_exists_for_length_k(k):
        hashes_indexes_map = {}
        h = 1
        for i in range(k - 1):
            h = (h * d) % q
        sub_str_hash = 0
        for i in range(k):
            sub_str_hash = (sub_str_hash * d + ord(A[i])) % q
        hashes_indexes_map[sub_str_hash] = [0]
        for i in range(1, n - k + 1):
            sub_str_hash = ((sub_str_hash - ord(A[i - 1]) * h) * d + ord(A[i - 1 + k])) % q
            if sub_str_hash in hashes_indexes_map:
                idxs = hashes_indexes_map[sub_str_hash]
                for idx in idxs:
                    if A[idx:idx + k] == A[i:i + k]:
                        return True
                hashes_indexes_map[sub_str_hash].append(i)
            else:
                hashes_indexes_map[sub_str_hash] = [i]
        return False

    left, right, ans = 1, n - 1, 0
    while left <= right:
        mid = (left + right) // 2
        if duplicate_exists_for_length_k(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
