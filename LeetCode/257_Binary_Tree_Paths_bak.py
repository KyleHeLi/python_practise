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

    def setParent(self, parentNode):
        self.parent = parentNode

    def setLeft(self, leftNode):
        self.left = leftNode

    def setRight(self, rightNode):
        self.right = rightNode

    def setVisited(self):
        self.visit = True

    def isVisited(self):
        return self.visit

    def getVal(self):
        return self.val

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent


class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}
    # parentPos = TreeNode(0)
    # curPos = TreeNode(0)
    # path = []
    # temp = ""
    # rightChildFlag = False
    def __init__(self, root):
        self.root = root
        self.root.setParent(TreeNode(0))
        self.parentPos = TreeNode(0)
        self.curPos = TreeNode(0)
        self.path = []
        self.temp = ""
        self.rightChildFlag = False
        self.count = 0

    def binaryTreePaths(self, root):
        if not root:
            return self.path
        else:
            if not root.isVisited():
                self.parentPos = self.curPos
                if not root.getParent():
                    self.temp += "->" + str(root.getVal())  
                    root.setParent(self.parentPos)       
                else:
                    self.temp += str(root.getVal())
            elif root.getRight() and root.getRight().isVisited():
                if root.getParent().getVal() == 0:
                    self.count += 1
                if self.count < 2:
                    return self.binaryTreePaths(self.root)
                else:
                    return self.path
            self.curPos = root
            self.curPos.setVisited()  
            if self.curPos.getLeft() and not self.curPos.getLeft().isVisited():
                self.rightChildFlag = False
                return self.binaryTreePaths(self.curPos.getLeft())
            elif self.curPos.getRight() and not self.curPos.getRight().isVisited():
                self.rightChildFlag = True
                return self.binaryTreePaths(self.curPos.getRight())
            else:
                self.path.append(self.temp)
                if self.rightChildFlag:                    
                    self.temp = self.temp[0:len(self.temp)-2*len("->")-len(str(self.curPos.getVal()))-len(str(self.curPos.getParent().getVal()))]
                    if self.curPos.getParent().getParent() and self.curPos.getParent().getParent().getVal() != 0:
                        return self.binaryTreePaths(self.curPos.getParent().getParent())
                    else:
                        self.binaryTreePaths(self.root)
                else:
                    self.temp = self.temp[0:len(self.temp)-len("->")-len(str(self.curPos.getVal()))]
                    return self.binaryTreePaths(self.curPos.getParent()) 
                # if self.parentPos.getLeft().isVisited():
                #     return self.path
                # else:
                #     if self.rightChildFlag:                    
                #         self.temp = self.temp[0:len(self.temp)-2*len("->")-len(str(self.curPos.getVal()))-len(str(self.curPos.getParent().getVal()))]
                #         self.binaryTreePaths(self.curPos.getParent().getParent())
                #     else:
                #         self.temp = self.temp[0:len(self.temp)-len("->")-len(str(self.curPos.getVal()))]
                #         self.binaryTreePaths(self.curPos.getParent()) 

        # if !root:     return None else:     if !root.isVisited():
        # grandParentPos = parentPos         parentPos = curPos
        # curPos = root     if curPos == self.root:         temp +=
        # (str) curPos.getVal()     else:         temp += "->" + (str)
        # curPos.getVal()     if curPos.getLeft():
        # rightChildFlag = False
        # binaryTreePaths(curPos.getLeft())     elif
        # curPos.getRight():         rightChildFlag = True
        # binaryTreePaths(curPos.getRight())     else:         if
        # rightChildFlag:             path.append(temp)
        # binaryTreePaths(grandParentPos)         else:
        # binaryTreePaths(ParentPos)      curPos.setVisited()



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
    import pdb; pdb.set_trace()  # breakpoint b7d83e47 //
    print test.binaryTreePaths(treeRoot)


if __name__ == '__main__':
    main()
