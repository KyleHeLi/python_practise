#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
        self.visit = False

    def setParent(parentNode):
        self.parent = parentNode

    def setLeft(leftNode):
        self.left = leftNode

    def setLeft(rightNode):
        self.right = rightNode

    def setVisited():
        self.visit = True

    def isVisited():
        return self.visit

    def getVal():
        return self.val

    def getLeft():
        return self.left

    def getRight():
        return self.right

    def getParent():
        return self.parent


class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}
    parentPos = TreeNode(0)
    # curPos = TreeNode(0)
    path = []
    temp = ""
    rightChildFlag = False
    def __init__(self, root):
        self.root = root
        root.setParent(TreeNode(0))

    def binaryTreePaths(self, root):
        if !root:
            return None
        else:
            if root.getParent().getVal() != 0:
                temp += "->" + (str) root.getVal()
                root.setParent(parentPos)
            else:
                temp += (str) root.getVal()
            if root.getLeft():
                rightChildFlag = False
                binaryTreePaths(root.getLeft())
            elif root.getRight():
                rightChildFlag = True
                binaryTreePaths(root.getRight())
            else:
                path.append(temp)
                if rightChildFlag:                    
                    temp = temp[0:len(temp)-2*len("->")-len((str)root.getVal())-len(str)root.]
                    binaryTreePaths(root.getLeft().getParent())
                else:
                    temp = temp[]
                    binaryTreePaths(root.getParent()) 
            root.setVisited()
            parentPos = root   
                



        # if !root:
        #     return None
        # else:
        #     if !root.isVisited():
        #         grandParentPos = parentPos
        #         parentPos = curPos
        #     curPos = root
        #     if curPos == self.root:
        #         temp += (str) curPos.getVal()
        #     else:
        #         temp += "->" + (str) curPos.getVal()
        #     if curPos.getLeft():
        #         rightChildFlag = False
        #         binaryTreePaths(curPos.getLeft())
        #     elif curPos.getRight():
        #         rightChildFlag = True
        #         binaryTreePaths(curPos.getRight())
        #     else:
        #         if rightChildFlag:
        #             path.append(temp)
        #             binaryTreePaths(grandParentPos)
        #         else:
        #             binaryTreePaths(ParentPos) 
        #     curPos.setVisited()



# Build a tree
# def buildATree(nodeList):
# 	if nodeList or nodeList[0] != None:
# 		for i in range(len(nodeList)):

# 	else:
# 		return None
# 	treeRoot = TreeNode(1)
#     node11 = TreeNode(2)
#     node12 = TreeNode(3)
#     node21 = TreeNode(4)
#     node22 = TreeNode(5)

    # return treeRoot

def main():
    treeRoot = TreeNode(1)
    node11 = TreeNode(2)
    node12 = TreeNode(3)
    # node21 = TreeNode(4)
    node22 = TreeNode(5)
    treeRoot.setLeft(node11)
    treeRoot.setRight(node12)
    node11.setRight(node22)

    test = Solution(treeRoot)
    print test.binaryTreePaths(treeRoot)


if __name__ == '__main__':
    main()
