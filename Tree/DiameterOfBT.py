# diameter_of_binary_tree_boilerplate.py
# Boilerplate only — no solution logic implemented.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traverseTree(node: Optional[TreeNode]):
            if not node:
                return 0
            
            left = traverseTree(node.left)
            right = traverseTree(node.right)

            nonlocal result
            result += max(result, left + right)
            return 1 + max(left, right)
        
        traverseTree(root)
        return result
        pass


def build_tree_from_list(values):
    """
    Builds a binary tree from a level-order list representation.
    Example: [1, 2, 3, None, 4]
    """
    if not values:
        return None

    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


if __name__ == "__main__":
    # Example test case (same format as LeetCode)
    tree_values = [1, 2, 3, 4, 5]
    root = build_tree_from_list(tree_values)

    sol = Solution()

    try:
        result = sol.diameterOfBinaryTree(root)
        print("Diameter:", result)
    except NotImplementedError as e:
        print(e)
