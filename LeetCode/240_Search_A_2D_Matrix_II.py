#!/usr/bin/env python
# -*- encoding:utf-8 -*-


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
            if not mList or mList[0] > target:
                break
            elif mList[-1] >= target:
                for x in mList:
                    if x == target:
                        return True
                    elif x > target:
                        break
        return False


def main():
    testMatrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
        []
    ]
    test = Solution()
    print test.searchMatrix(testMatrix, 5)
    print test.searchMatrix(testMatrix, 20)


if __name__ == '__main__':
    main()
