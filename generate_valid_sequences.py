def generate_valid_sequences(n):
    ans = []

    def rec_helper(curr, res):
        if len(curr) == n:
            res.append(curr)
            return

        if not (len(curr) >= 2 and curr[-2:] == [0, 0]):
            rec_helper(curr + [0], res)
        rec_helper(curr + [1], res)

    rec_helper([], ans)
    print(len(ans))
    for seq in ans:
        print(seq)


generate_valid_sequences(7)
