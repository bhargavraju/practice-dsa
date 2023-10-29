"""AVL Tree implementation"""


class Node:

    def __init__(self, val):
        self.val = val
        self.height = 0
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def balancing_factor(node):
    if node is None:
        return 0
    else:
        return height(node.left) - height(node.right)


def left_rotate(node):
    right = node.right
    right_left = right.left
    right.left = node
    node.right = right_left
    node.height = 1 + max(height(node.left), height(node.right))
    right.height = 1 + max(height(right.left), height(right.right))
    return right


def right_rotate(node):
    left = node.left
    left_right = left.right
    left.right = node
    node.left = left_right
    node.height = 1 + max(height(node.left), height(node.right))
    left.height = 1 + max(height(left.left), height(left.right))
    return left


def balance_fix(node):
    balance = balancing_factor(node)
    if balance > 1:
        left_balance = balancing_factor(node.left)
        if left_balance < 0:
            node.left = left_rotate(node.left)
        node = right_rotate(node)
    elif balance < -1:
        right_balance = balancing_factor(node.right)
        if right_balance > 0:
            node.right = right_rotate(node.right)
        node = left_rotate(node)
    return node


def insert(val, node):
    if node is None:
        return Node(val)
    if val <= node.val:
        node.left = insert(val, node.left)
    else:
        node.right = insert(val, node.right)
    node.height = 1 + max(height(node.left), height(node.right))
    node = balance_fix(node)
    return node


def successor(node):
    while node.left is not None:
        node = node.left
    return node


def delete(val, node):
    if node is None:
        return node
    if val > node.val:
        node.right = delete(val, node.right)
    elif val < node.val:
        node.left = delete(val, node.left)
    else:
        if node.right is None:
            return node.left
        elif node.left is None:
            return node.right
        next_node = successor(node.right)
        node.val = next_node.val
        node.right = delete(next_node.val, node.right)
    node.height = 1 + max(height(node.left), height(node.right))
    node = balance_fix(node)
    return node


def traverse_preorder(node):
    if node is None:
        return
    print(node.val)
    if node.left:
        traverse_preorder(node.left)
    if node.right:
        traverse_preorder(node.right)


nd = insert(1, None)
print('first traversal')
traverse_preorder(nd)
# nd = insert(2, nd)
# print('second traversal')
# traverse_preorder(nd)
# nd = insert(3, nd)
# print('third traversal')
# traverse_preorder(nd)
# nd = insert(4, nd)
# print('fourth traversal')
# traverse_preorder(nd)
# nd = insert(5, nd)
# print('fifth traversal')
# traverse_preorder(nd)
# nd = insert(6, nd)
# print('sixth traversal')
# traverse_preorder(nd)
# nd = insert(7, nd)
# print('seventh traversal')
# traverse_preorder(nd)
# nd = insert(8, nd)
# print('eighth traversal')
# traverse_preorder(nd)
# nd = insert(9, nd)
# print('ninth traversal')
# traverse_preorder(nd)
# nd = insert(10, nd)
# print('tenth traversal')
# traverse_preorder(nd)
# nd = delete(9, nd)
# nd = delete(10, nd)
nd = delete(1, nd)
print('delete traversal')
traverse_preorder(nd)
