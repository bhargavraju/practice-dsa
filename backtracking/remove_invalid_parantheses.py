# @param A : string
# @return a list of strings
def solve(A):
    def min_invalid(s):
        st = []
        for ch in s:
            if ch == '(':
                st.append(ch)
            elif ch == ')':
                if len(st) == 0:
                    st.append(ch)
                elif st[-1] == '(':
                    st.pop()
                else:
                    st.append(ch)
        return len(st)

    def is_valid(s):
        return min_invalid(s) == 0

    required_removals = min_invalid(A)

    def rec_helper(s, i, removals, res):
        if removals == required_removals:
            if is_valid(s) and s not in res:
                res.add(s)
            return
        if i == len(s):
            return

        for idx in range(i, len(s)):
            if s[idx] in ['(', ')']:
                rec_helper(s[:idx] + s[idx+1:], idx, removals + 1, res)

    ans = set()
    rec_helper(A, 0, 0, ans)
    return list(ans)
