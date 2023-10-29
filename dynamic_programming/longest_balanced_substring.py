"""
Given a string A made up of multiple brackets of type "[]" , "()" and "{}"
find the length of the longest substring which forms a balanced string .

Conditions for a string to be balanced :
Blank string is balanced
( However blank string will not be provided as a test case ).
If B is balanced : (B) , [B] and {B} are also balanced.
If B1 and B2 are balanced then B1B2 i.e the string formed by concatenating
B1 and B2 is also balanced.

Problem Constraints
0 <= |A| <= 10^6

Input Format
First and only argument is an string A.

Output Format
Return an single integer denoting the lenght of the longest balanced substring.
"""


# Solving using kadence algorithm
# Create dp array which stores max balanced substring ending with that index
# (i) If i is open, then value is automatically 0 else
# (ii) If i is closed and i-1 is open and matches then dp[i-2] + 2
# (iii) If i is closed and i-1 is closed, consider the balanced substring
# ending with i-1 and get the character just before that substring
# (prev_unbalanced_index). If it is open and matches then we can add 2 to
# dp[i-1]. Since B1B2 is also balanced if B1 and B2 are balanced, we also add
# dp[prev_unbalanced_index-1]


def is_match(closing, opening):
    if closing == ']' and opening == '[':
        return True
    if closing == ')' and opening == '(':
        return True
    if closing == '}' and opening == '{':
        return True
    return False


def is_opening(el):
    if el in ['[', '(', '{']:
        return True
    return False


def is_closing(el):
    if el in [']', ')', '}']:
        return True
    return False


class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        n = len(A)
        max_substring = [0] * n
        for i in range(1, n):
            if is_opening(A[i]):
                continue
            if is_opening(A[i - 1]):
                if is_match(A[i], A[i - 1]):
                    max_substring[i] = (max_substring[i - 2] if i - 2 >= 0 else 0) + 2
            else:
                prev_max_length = max_substring[i - 1]
                prior_element_index = i - prev_max_length - 1
                if prior_element_index >= 0:
                    if is_match(A[i], A[prior_element_index]):
                        max_substring[i] = 2 + max_substring[i - 1] + (max_substring[prior_element_index - 1] if prior_element_index - 1 >= 0 else 0)
        return max(max_substring)
