"""
You are given the task of ranking hotel reviews in this question.

Lets say, you are given a bunch of user reviews where each review is a string.
Assume that our Expedia bots have figured out a set of "Good words"
which indicate that the user likes the hotel.
The more the number of "Good words", the more the user likes the hotel.

Given multiple such reviews and the list of good words, you need to rank
the reviews with the most positive review first and
the most negative review the last.
In other words, the review with the most number of good words comes first and
the one with least number of good words comes last in the ranking.

Note: Sorting should be stable. If review i and review j have the
same number of "Good words", then their original order would be preserved.

Constraints:
1.   1 <= No.of reviews <= 200
2.   1 <= No. of words in a review <= 1000
3.   1 <= Length of an individual review <= 10,000
4.   1 <= Number of Good Words <= 10,000
5.   1 <= Length of an individual Good Word <= 4
6.   All the alphabets are lower case (a - z)

Input:
S : A string S containing "Good Words" separated by  "_" character.
R : A vector of strings containing Hotel Reviews.
    Review strings are also separated by "_" character.

Output:
A vector V of integer which contain the original indexes of the reviews in
the sorted order of reviews.

V[i] = k  means the review R[k] comes at i-th position in the sorted order.
In simple words, V[i]=Original index of the review which comes at
i-th position in the sorted order. (Indexing is 0 based)

Example:

Input:
S = "pool_fridge_wifi"
R = ["water_in_pool", "pond_fridge_drink", "pool_wifi_speed"]

Output:
ans = [2, 0, 1]
sorted reviews are ["pool_wifi_speed", "water_in_pool", "pond_fridge_drink"]

"""


class Trie:

    def __init__(self, val):
        self.val = val
        self.children = []
        self.final = False


def insert(trie, word):
    curr = trie
    for ch in word:
        for child in curr.children:
            if child.val == ch:
                curr = child
                break
        else:
            node = Trie(ch)
            curr.children.append(node)
            curr = node
    curr.final = True


def is_matching(trie, word):
    curr = trie
    for ch in word:
        for child in curr.children:
            if child.val == ch:
                curr = child
                break
        else:
            return False

    if curr.final is not True:
        return False
    return True


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        good_words_trie = Trie('$')
        good_words = A.split('_')
        for good_word in good_words:
            insert(good_words_trie, good_word)
        matches = []
        for idx, review in enumerate(B):
            match_count = 0
            review_words = review.split('_')
            for review_word in review_words:
                if is_matching(good_words_trie, review_word):
                    match_count += 1
            matches.append((idx, match_count))
        sorted_matches = sorted(matches, key=lambda match: match[1],
                                reverse=True)
        res = [sorted_match[0] for sorted_match in sorted_matches]
        return res
