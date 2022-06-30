
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):

        if root:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
            return root
        return None

    def maxDepth(self,root):
        # if root:
        #     return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
        # return None
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

    def diameterOfBinaryTree(self, root):
        res = [0]

        def dfs(root):
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                res[0] = max(res[0],2+left+right)

                return 1+max(left,right)

            return -1

        dfs(root)
        return res[0]

    def isBalanced(self,root) -> bool:

        def dfs(root):

            if root:
                left,right = dfs(root.left),dfs(root.right)
                balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)

                return [balanced,1+max(left[1],right[1])]

            return [True,0]

        return dfs(root)[0]

    def isSameTree(self,p,q) -> bool:

        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSubTree(self,s,t) -> bool:

        if not t:
            return True
        if not s:
            return False

        if self.isSameTree(s, t):
            return True

        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))


    def lowestCommonAncestor(self, root, p, q):

        res = None

        if not root or not p or not q:
            return None

        def search(root, p, q):

            if not root:
                return False

            mid = left = right = False

            if root.val == p.val or root.val == q.val:
                mid = True

            left = search(root.left, p, q)
            right = search(root.right, p, q)

            if mid:
                if left or right:
                    self.res = root

            elif left and right:
                self.res = root

            return mid or left or right

        search(root, p, q)
        return self.res
