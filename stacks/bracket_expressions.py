"""
Given two strings A and B. Each string represents an expression consisting
of lowercase english alphabets, '+', '-', '(' and ')'. The task is to compare
them and check if they are similar. If they are similar return 1 else return 0.

NOTE: It may be assumed that there are at most 26 operands from ‘a’ to ‘z’
and every operand appears only once.

Problem Constraints
1 <= length of the each String <= 100

Example Input

Input 1:
 A = "-(a+b+c)"
 B = "-a-b-c"
Input 2:
 A = "a-b-(c-d)"
 B = "a-b-c-d"

Example Output

Output 1:
 1
Output 2:
 0
"""


def evaluate(expr):
    st = [True]
    char_map = {}
    for i in range(len(expr)):
        ch = expr[i]
        if ch == '(':
            if i > 0 and expr[i-1] == '-':
                st.append(not st[-1])
            else:
                st.append(st[-1])
        elif ch == ')':
            st.pop()
        elif ch in '+-':
            continue
        else:
            global_sign = st[-1]
            local_sign = True
            if i > 0 and expr[i-1] == '-':
                local_sign = False
            final_sign = local_sign == global_sign
            char_map[ch] = final_sign

    return char_map


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        return int(evaluate(A) == evaluate(B))
