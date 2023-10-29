"""
An arithmetic expression is given by a charater array A of size N. Evaluate the value of an arithmetic expression
in Reverse Polish Notation.

Valid operators are +, -, *, /. Each character may be an integer or an operator.

Example Input
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Input 2:
    A = ["4", "13", "5", "/", "+"]


Example Output
Output 1:
    9
Output 2:
"""


# @param A : list of strings
# @return an integer
def evalRPN(A):
    def operation(symbol, el1, el2):
        if symbol == '+':
            return int(el1) + int(el2)
        elif symbol == '-':
            return int(el1) - int(el2)
        elif symbol == '*':
            return int(el1) * int(el2)
        else:
            return int(el1) // int(el2)

    st = []
    for el in A:
        if el in ['+', '-', '*', '/']:
            el2 = st.pop()
            el1 = st.pop()
            st.append(str(operation(el, el1, el2)))

        else:
            st.append(el)

    return int(st[0])
