"""
Find out the number of A digit positive numbers, whose digits on being added
equals to a given number B. Note that a valid number starts from digits 1-9
except the number 0 itself. i.e. leading zeroes are not allowed.

Since the answer can be large, output answer modulo 1000000007

Problem Constraints
1 <= A <= 1000
1 <= B <= 10000
"""

# num < j condition instead of num <= j because dp[i][0] is 0 except for i = 1,
# which cannot be counted because that would result in a leading zero case


# @param A : integer
# @param B : integer
# @return an integer
def solve(A, B):
    if B > 9*A:
        return 0
    dp = [[0]*(B+1) for _ in range(A+1)]
    dp[1][0] = 1
    for i in range(1, A+1):
        for j in range(1, B+1):
            if i == 1 and 1 <= j <= 9:
                dp[i][j] = 1
                continue
            for num in range(10):
                if num < j:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-num]) % 1000000007
    return dp[A][B]
