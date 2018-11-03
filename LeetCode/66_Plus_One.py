#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carryFlag = False
        if not digits:
            return False
        for i in range(len(digits)):
            if digits[-1 - i] < 0:
                return False
            if digits[-1 - i] + 1 >= 10:
                carryFlag = True
                digits[-1 - i] = 0
            else:
                digits[-1 - i] += 1
                carryFlag = False
                break

        if carryFlag:
            digits.insert(0, 1)

        return digits


def main():
    # [1, 3]
    numList1 = [1, 2]
    # [2, 0]
    numList2 = [1, 9]
    # [1, 2, 9]
    numList3 = [1, 2, 9]
    numList4 = [1, 9, 9]
    numList5 = [9, 9]
    numList6 = [2]
    numList7 = [9]
    numList8 = [0]
    numList9 = [-1]

    test = Solution()
    print(test.plusOne(numList1))
    print(test.plusOne(numList2))
    print(test.plusOne(numList3))
    print(test.plusOne(numList4))
    print(test.plusOne(numList5))
    print(test.plusOne(numList6))
    print(test.plusOne(numList7))
    print(test.plusOne(numList8))
    print(test.plusOne(numList9))


if __name__ == '__main__':
    main()
