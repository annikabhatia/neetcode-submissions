# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        curr = root
        while curr:
            #if both values are greater than root, search the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            #else, search the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            #else, the current element is the root, so return the root
            else:
                return curr


        