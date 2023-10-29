"""
Two persons are playing a word game where players alternate appending letters
to a word. The person who spells out a word, or creates a prefix for which
there is no continuation possible, loses.

Given a dictionary of words denoted by string array A, determine the letters
the first player should start with, such that with the optimal play they
cannot lose.

NOTE: If no letter satisfies the above condition, return a character array
with only character '0'.

Problem Constraints
1 <= length of A <= 10^5
1 <= Sum of length of all words <= 106
Words consist of only lowercase letters
"""


class TrieNode:

    def __init__(self, char):
        self.char = char
        self.children = []


def add_word_to_trie(word, trie):
    curr = trie
    for ch in word:
        for child in curr.children:
            if child.char == ch:
                curr = child
                break
        else:
            new_node = TrieNode(ch)
            curr.children.append(new_node)
            curr = new_node


def rec_helper(node, turn):
    if not node.children:
        if turn == 1:
            return False
        else:
            return True
    if turn == 1:
        possible = True
        for child in node.children:
            possible = possible and rec_helper(child, 0)
    else:
        possible = False
        for child in node.children:
            possible = possible or rec_helper(child, 1)

    return possible


# @param A : list of strings
# @return a list of characters
def solve(A):
    trie = TrieNode('$')
    for word in A:
        add_word_to_trie(word, trie)
    res = []
    for node in trie.children:
        if rec_helper(node, 1):
            res.append(node.char)
    if res:
        return sorted(res)
    return ['0']
