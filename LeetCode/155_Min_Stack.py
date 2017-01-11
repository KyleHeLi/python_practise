#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackList = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stackList.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        self.stackList.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stackList[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stackList) == 0:
            return None
        else:
            return self.stackList[-1][1]


def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.push(-1)
    # Returns -3
    print minStack.getMin()
    minStack.pop()
    # Returns 0
    print minStack.top()
    # Returns -2
    print minStack.getMin()


if __name__ == '__main__':
    main()
