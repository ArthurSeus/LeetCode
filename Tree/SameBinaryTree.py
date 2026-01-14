# same_binary_tree_boilerplate.py
# Boilerplate only — no solution logic implemented.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # TODO: implement solution
        raise NotImplementedError("Implement isSameTree")


def build_tree_from_list(values):
    """
    Builds a binary tree from a level-order list representation.
    Example: [1, 2, 3]
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
    p_values = [1, 2, 3]
    q_values = [1, 2, 3]

    p_root = build_tree_from_list(p_values)
    q_root = build_tree_from_list(q_values)

    sol = Solution()

    try:
        result = sol.isSameTree(p_root, q_root)
        print("Are same tree:", result)
    except NotImplementedError as e:
        print(e)
