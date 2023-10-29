"""
Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1.
Now given a string representing A, you should return the smallest good base of A in string format.

Input Format
The only argument given is the string representing A.

Output Format
Return the smallest good base of A in string format.

Constraints
3 <= A <= 10^18

Solution explanation: A number with all ones in it's base k form will be a sum of geometric series
1 + base + base^2 + base^3 +.... base^(d-1) where d is the no of 1s (length of it's base k form)
So, use the formula to check the values

max possible value of base = number-1 where d = 1
"""


# @param A : string
# @return a strings
def solve(A):
    d = 2
    A = int(A)
    ans = A - 1
    while pow(2, d) <= A + 1:
        left, right = 2, A - 1
        while left <= right:
            base = (left + right) // 2
            calc = (pow(base, d) - 1) // (base - 1)
            if calc == A:
                ans = min(ans, base)
                right = base - 1
            elif calc > A:
                right = base - 1
            else:
                left = base + 1
        d += 1
    return ans
