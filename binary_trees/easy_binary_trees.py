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
    
    def isBalanced(self, root):     
        def dfs(root):
            if root is None:
                return [True, 0]

            #traverse the subtrees and count the depth
            left = dfs(root.left)
            right = dfs(root.right)

            
            # Check if the current subtree is balanced:
            # 1. Left subtree is balanced
            # 2. Right subtree is balanced
            # 3. The height difference between left and right is at most 1
            balanced = (left[0] and right[0] and 
                abs(left[1]-right[1]) <=1)
                
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


    #function that compares two binary trees and checks that they are the same
    def isSameTree(self, p, q) -> bool:

        #if both trees are empty then they are the same
        if p is None and q is None:
            return True 

        #if both trees are non-empty and have the same values then traverse the left and right subtress of both trees
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


    #function to check that if a fixed subtree exists in the binary tree 
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True

        #if we dont have a root and we have a subroot then its false
        if root is None and subRoot:
            return False

        #call isSameTree to check that if the tree values are the same
        if self.isSameTree(root, subRoot):
            return True

        #check left and right subtree of root since the subroot is fixed
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
