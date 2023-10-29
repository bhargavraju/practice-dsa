"""
Given an expression string A, examine whether the pairs and the orders of
“{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.
Refer to the examples for more clarity.

Problem Constraints
1 <= |A| <= 100

Input Format
The first and the only argument of input contains the string A having
the paranthesis sequence.

Output Format
Return 0, if the paranthesis sequence is not balanced.
Return 1, if the paranthesis sequence is balanced.

Example Input
Input 1:
 A = {([])}

Input 2:
 A = (){

Input 3:
 A = ()[]

Example Output
Output 1:
 1

Output 2:
 0

Output 3:
 1
"""


# @param A : string
# @return an integer
def solve(A):
    st = []
    for ch in A:
        if ch in ['(', '{', '[']:
            st.append(ch)
        else:
            if len(st) == 0:
                return 0
            top = st.pop()
            if (ch == ')' and top != '(') or (ch == '}' and top != '{') or (
                    ch == ']' and top != '['):
                return 0

    if len(st) > 0:
        return 0

    return 1
