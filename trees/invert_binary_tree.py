from typing import Optional

"""
[EASY] INVERT BINARY TREE
https://neetcode.io/problems/invert-a-binary-tree

Date: 18th Apr 2026
Author: Diya Ramesh

Time: O(n)
    - where n = #nodes in the tree
Space: O(n)
    - where n = #nodes in the tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    tmp = root.right
    root.right = root.left
    root.left = tmp


    self.invertTree(root.left)
    self.invertTree(root.right)

    return root