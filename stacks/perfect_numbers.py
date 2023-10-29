"""
Given an integer A, you have to find the Ath Perfect Number.

A Perfect Number has the following properties:
It comprises only 1 and 2.
The number of digits in a Perfect number is even.
It is a palindrome number.

For example 11, 22, 112211 are Perfect numbers, where 123, 121, 782, 1 are not.

Example Input

Input 1:
 A = 2
Input 2:
 A = 3

Example Output

Output 1:
 22
Output 2:
 1111

First four perfect numbers are:
1. 11
2. 22
3. 1111
4. 1221
"""


# @param A : integer
# @return a strings
def solve(A):
    queue = ['1', '2']
    i = 1
    val = '1'
    while True:
        el = queue.pop(0)
        if i == A:
            val = el
            break
        new_elements = [el + '1', el + '2']
        queue += new_elements
        i += 1
    return val + val[::-1]
