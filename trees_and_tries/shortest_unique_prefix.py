"""
Given a list of N words.
Find shortest unique prefix to represent each word in the list.

NOTE: Assume that no word is prefix of another.
In other words, the representation is always possible

Problem Constraints
1 <= Sum of length of all words <= 10^6
"""


class TrieNode:

    def __init__(self, val, count):
        self.val = val
        self.count = count
        self.children = []


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        trie = TrieNode('$', 0)
        for word in A:
            curr = trie
            for ch in word:
                for child in curr.children:
                    if child.val == ch:
                        child.count += 1
                        curr = child
                        break
                else:
                    child = TrieNode(ch, 1)
                    curr.children.append(child)
                    curr = child

        result = []
        for word in A:
            curr = trie
            curr_prefix = ''
            for ch in word:
                found = False
                curr_prefix += ch
                for child in curr.children:
                    if child.val == ch:
                        curr = child
                        if child.count == 1:
                            found = True
                            break
                if found is True:
                    result.append(curr_prefix)
                    break

        return result
