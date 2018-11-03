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

    def __init__(self, root):
        self.root = root
        self.root.setParent(TreeNode(0))
        self.parentPos = TreeNode(0)
        self.curPos = TreeNode(0)
        self.path = []
        self.temp = ""
        self.rightChildFlag = False

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
            elif root.getParent().getVal() == 0:
                if not root.getRight() or root.getRight() and root.getRight().isVisited():
                    return self.path
                else:
                    self.curPos = root
                    return self.binaryTreePaths(self.curPos.getRight())
            self.curPos = root 
            self.curPos.setVisited() 
            if self.curPos.getParent().getLeft() and self.curPos.getParent().getLeft().getVal() == self.curPos.getVal():
                self.rightChildFlag = False
            elif self.curPos.getParent().getRight() and self.curPos.getParent().getRight().getVal() == self.curPos.getVal():
                self.rightChildFlag = True
            if self.curPos.getLeft() and not self.curPos.getLeft().isVisited():
                # self.rightChildFlag = False
                return self.binaryTreePaths(self.curPos.getLeft())
            elif self.curPos.getRight() and not self.curPos.getRight().isVisited():
                # self.rightChildFlag = True
                return self.binaryTreePaths(self.curPos.getRight())
            else:
                if self.curPos.getRight() or self.curPos.getLeft():
                    pass
                else:
                    self.path.append(self.temp)
                if self.rightChildFlag:                    
                    self.temp = self.temp[0:len(self.temp)-2*len("->")-len(str(self.curPos.getVal()))-len(str(self.curPos.getParent().getVal()))]
                    if self.curPos.getParent().getParent() and self.curPos.getParent().getParent().getVal() != 0:
                        return self.binaryTreePaths(self.curPos.getParent().getParent())
                    else:
                        self.temp = '1'
                        return self.binaryTreePaths(self.root)
                else:
                    self.temp = self.temp[0:len(self.temp)-len("->")-len(str(self.curPos.getVal()))]
                    return self.binaryTreePaths(self.curPos.getParent()) 


def main():
    # Case 1
    # treeRoot = TreeNode(1)
    # node11 = TreeNode(2)
    # node12 = TreeNode(3)
    # node21 = TreeNode(4)
    # node22 = TreeNode(5)
    # treeRoot.setLeft(node11)
    # treeRoot.setRight(node12)
    # node11.setLeft(node21)
    # node11.setRight(node22)

    # Case 2
    # treeRoot = TreeNode(1)
    # node11 = TreeNode(2)
    # node12 = TreeNode(3)
    # node21 = TreeNode(4)
    # node22 = TreeNode(5)
    # node31 = TreeNode(6)
    # node41 = TreeNode(7)
    # node42 = TreeNode(8)
    # treeRoot.setLeft(node11)
    # treeRoot.setRight(node12)
    # node11.setLeft(node21)
    # node11.setRight(node22)
    # node22.setRight(node31)
    # node31.setLeft(node41)
    # node31.setRight(node42) 

    # Case 3
    # treeRoot = TreeNode(1)
    # node11 = TreeNode(2)
    # node21 = TreeNode(3)
    # node22 = TreeNode(4)
    # node31 = TreeNode(5)
    # node41 = TreeNode(6)
    # node51 = TreeNode(7)
    # treeRoot.setLeft(node11)
    # node11.setLeft(node21)
    # node11.setRight(node22)
    # node22.setRight(node31)
    # node31.setRight(node41)
    # node41.setRight(node51) 

    # Case 4
    treeRoot = TreeNode(1)
    node02 = TreeNode(2)
    node03 = TreeNode(3)
    node04 = TreeNode(4)
    node05 = TreeNode(5)
    node06 = TreeNode(6)
    node07 = TreeNode(7)
    node08 = TreeNode(8)
    node09 = TreeNode(9)
    node10 = TreeNode(10)
    node11 = TreeNode(11)
    node12 = TreeNode(12)
    node13 = TreeNode(13)
    node14 = TreeNode(14)
    node15 = TreeNode(15)
    node16 = TreeNode(16)
    node17 = TreeNode(17)
    node18 = TreeNode(18)
    node19 = TreeNode(19)
    treeRoot.setLeft(node02)
    treeRoot.setRight(node03)
    node02.setLeft(node04)
    node02.setRight(node10)
    node03.setRight(node11)
    node04.setLeft(node05)
    node04.setRight(node06)
    node05.setRight(node07)
    node06.setLeft(node09)
    node07.setRight(node08)
    node11.setLeft(node12)
    node11.setRight(node13)
    node12.setRight(node14)
    node12.setLeft(node17)
    node14.setRight(node15)
    node15.setRight(node16)
    node17.setLeft(node18)
    node18.setLeft(node19)


    test = Solution(treeRoot)
    print(test.binaryTreePaths(treeRoot))


if __name__ == '__main__':
    main()
