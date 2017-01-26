#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
        	return False
        for mList in matrix:
            if mList and target <= mList[-1]:
                if target in mList:
                    return True
            else:
                continue
        return False


def main():
    testMatrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
        []
    ]
    target = 51
    test = Solution()
    print test.searchMatrix(testMatrix, target)


if __name__ == '__main__':
    main()
