# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    #inverting the tree using DFS (Depth first search)
    def invertTree(self, root):

        #if we have an empty root
        if root is None:
            return None

        #swap children
        temp = root.left
        root.left = root.right
        root.right = temp

        #traverse the tree left node then right node
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    def invertTree2(self, root):

        #if we have an empty root
        if root is None:
            return None

        #swap children this way without a need for a temp variable
        root.left, root.right = root.right, root.left

        #traverse the tree left node then right node
        self.invertTree2(root.left)
        self.invertTree2(root.right)
        return root

    def maxDepth(self, root):
    # Base case: if the current node is None, the depth is 0
        if root is None:
            return 0

        #traverse through the left and right subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # Return the maximum of the two depths plus 1 for the current node
        return 1+max(left, right)


    def diameterOfBinaryTree(self, root):
        #global variable
        self.res = 0

        #use depth first search, curr is the current node
        def dfs(curr):
            if not curr:
                return 0

            #traverse the subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)

            #The diameter at the current node is the sum of left and right depths
            self.res = max(self.res, left+right)

            #Return the depth of the current node (max depth of subtrees + 1)
            return max(left,right) + 1

        dfs(root)
        return self.res
        


