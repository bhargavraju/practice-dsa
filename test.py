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
        if rec_helper(node, trie):
            res.append(node.char)
    if res:
        return sorted(res)
    return ['0']


test_arr = [ "cat", "calf", "dog", "bear" ]
print(solve(test_arr))
