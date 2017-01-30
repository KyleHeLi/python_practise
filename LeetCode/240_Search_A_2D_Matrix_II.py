#!/usr/bin/env python
# -*- encoding:utf-8 -*-


class Solution(object):

    # Own solution
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

    # Top solution
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix:
            m, n, r, c = len(matrix), len(matrix[0]), 0, len(matrix[0]) - 1
            while r < m and c >= 0:
                if not matrix[r] or matrix[r][c] < target:
                    r += 1
                elif matrix[r][c] == target:
                    return True
                else:
                    c -= 1
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
    print test.searchMatrix1(testMatrix, 5)
    print test.searchMatrix1(testMatrix, 20)


if __name__ == '__main__':
    main()
