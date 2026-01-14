# balanced_binary_tree_boilerplate.py
# Boilerplate only — no solution logic implemented.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(curr: Optional[TreeNode]):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if (left - right > 1 or left - right < -1):
                self.balanced = False

            return 1 + max(right, left)
        
        dfs(root)
        return self.balanced
        pass


def build_tree_from_list(values):
    """
    Builds a binary tree from a level-order list representation.
    Example: [1, 2, 3, None, None, 4]
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
    # Example test case from the problem
    tree_values = [1,2,3,None,None,4,None,5]
    root = build_tree_from_list(tree_values)

    sol = Solution()

    try:
        result = sol.isBalanced(root)
        print("Is balanced:", result)
    except NotImplementedError as e:
        print(e)
