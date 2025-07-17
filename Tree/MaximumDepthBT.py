# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

# Função auxiliar para criar árvore a partir de lista
def build_tree(nodes):
    from collections import deque
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1
    while i < len(nodes):
        current = q.popleft()
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            q.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            q.append(current.right)
        i += 1
    return root

# Teste com a entrada fornecida
root_list = [1, 2, 3, None, None, None, 4]
root = build_tree(root_list)

sol = Solution()
depth = sol.maxDepth(root)
print("Max Depth:", depth)
