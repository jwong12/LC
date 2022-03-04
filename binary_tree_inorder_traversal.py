
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Input: root = [1,null,2,3]
# Output: [1,3,2]
def inorder_traversal(res, root):
    if not root:
        return

    inorder_traversal(res, root.left)
    res.append(root.val)
    inorder_traversal(res, root.right)


def inorder_traversal_iter(root):
    stack = []
    res = []
    curr = root
    while curr or stack:
        # add all left nodes into stack
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right

    return res


if __name__ == "__main__":
    node3 = Node(3)
    node2 = Node(2, left=node3)
    node1 = Node(1, right=node2)
    results = []
    inorder_traversal(results, node1)
    print(results)
    print(inorder_traversal_iter(node1))

