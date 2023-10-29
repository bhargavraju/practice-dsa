"""
Given a String A and an integer B. String A is encoded consisting of lowercase English letters and numbers.
A is encoded in a way where repetitions of substrings are represented as substring followed by the count of substrings.

For example: if the encrypted string is “ab2cd2” and B=6, so the output will be ‘d’ because the decrypted string is
“ababcdababcd” and 4th character is ‘b’.

You have to find and return the Bth character in the decrypted string.

Note: Frequency of encrypted substring can be of more than one digit. For example, in “ab12c3”, ab is repeated 12 times.
No leading 0 is present in the frequency of substring.


Constraints
1 <= length of the array <= 10^5
1 < = K < = 10^9

For Example

Input 1:
    A = "ab2c3"
    B = 8
Output 1:
    a
    Decrypted string will be "ababcababcababc" and 'a' is the 8th character.

Input 2:
    A = "x2y3"
    B = 3
Output 2:
    y
    Decrypted string will be "xxyxxyxxy"
"""


# @param A : string
# @param B : integer
# @return a strings
def solve(A, B):
    n = len(A)
    st = []
    i = 0
    prev_times = 0
    while i < n:
        j = i
        while j < n and A[j].isalpha():
            j += 1
        ch = A[i:j]
        k = j
        while k < n and A[k].isdigit():
            k += 1
        times = 1 if j == k else int(A[j:k])
        if len(st) > 0:
            prev_idx = st[-1][1]
            curr_idx = prev_idx * prev_times + len(ch)
            st.append((ch, curr_idx))
        else:
            st.append((ch, len(ch)))
        prev_times = times
        i = k
    rem = B
    while len(st) > 0:
        ch, idx = st.pop()
        rem = rem % idx
        if rem == 0:
            return ch[-1]
        elif idx - len(ch) < rem < idx:
            return ch[rem - idx + len(ch) - 1]
