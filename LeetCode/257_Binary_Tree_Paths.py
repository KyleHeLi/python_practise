#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}

    # Recursive solution
    def binaryTreePaths(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]

    # dfs + stack
    def binaryTreePaths1(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            # print stack
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res
        
    # bfs + queue
    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res
        
    # # dfs recursively
    # def binaryTreePaths(self, root):
    #     if not root:
    #         return []
    #     res = []
    #     self.dfs(root, "", res)
    #     return res

    # def dfs(self, root, ls, res):
    #     if not root.left and not root.right:
    #         res.append(ls+str(root.val))
    #     if root.left:
    #         self.dfs(root.left, ls+str(root.val)+"->", res)
    #     if root.right:
    #         self.dfs(root.right, ls+str(root.val)+"->", res)


# def buildTree(treeList):
#     root = TreeNode(1)
#     temp
#     for node in treeList:
#         if node:



def main():
    # case 1
    # testList = [1,2,3,4,5,None,None]
    # treeRoot = TreeNode(1)
    # treeRoot.left = TreeNode(2)
    # treeRoot.right = TreeNode(3)
    # treeRoot.left.left = TreeNode(4)
    # treeRoot.left.right = TreeNode(5)
    
    # case 2
    testList = [1,2,3,4,10,None,11,5,6,None,None,12,13,None,7,9,None,17,14,None,None,None,8,None,None,18,None,None,15,None,None,19,None,None,16]
    treeRoot = TreeNode(1)
    treeRoot.left = TreeNode(2)
    treeRoot.right = TreeNode(3)
    treeRoot.left.left = TreeNode(4)
    treeRoot.left.right = TreeNode(10)
    treeRoot.right.right = TreeNode(11)
    treeRoot.left.left.left = TreeNode(5)
    treeRoot.left.left.right = TreeNode(6)
    treeRoot.right.right.left = TreeNode(12)
    treeRoot.right.right.right = TreeNode(13)
    treeRoot.left.left.left.right = TreeNode(7)
    treeRoot.left.left.right.left = TreeNode(9)
    treeRoot.left.left.left.right.right = TreeNode(8)
    treeRoot.right.right.left.left = TreeNode(17)
    treeRoot.right.right.left.right = TreeNode(14)
    treeRoot.right.right.left.left.left = TreeNode(18)
    treeRoot.right.right.left.left.left.left = TreeNode(19)
    treeRoot.right.right.left.right.right = TreeNode(15)
    treeRoot.right.right.left.right.right.right = TreeNode(16)
    
    test = Solution()
    print(test.binaryTreePaths1(treeRoot))


if __name__ == '__main__':
    main()