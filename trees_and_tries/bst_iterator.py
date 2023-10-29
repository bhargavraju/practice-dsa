"""
Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

The first call to next() will return the smallest number in BST.
Calling next() again will return the next smallest number in the BST,
and so on.

 Note: next() and hasNext() should run in average O(1) time and
 uses O(h) memory, where h is the height of the tree.
 Try to optimize the additional space complexity apart from the
 amortized time complexity.
"""


class BSTIterator:
    def add_node_left_successors(self, node):
        if node is None:
            return

        self.st.append(node)
        left_child = node.left

        while left_child:
            self.st.append(left_child)
            left_child = left_child.left

    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.st = []
        self.add_node_left_successors(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.st) > 0

    # @return an integer, the next smallest number
    def next(self):
        el = self.st.pop()
        if el.right:
            self.add_node_left_successors(el.right)
        return el.val

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
