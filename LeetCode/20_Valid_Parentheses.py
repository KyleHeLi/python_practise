#!/usr/bin/env python
# -*- encoding:utf-8 -*-


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stackLeftBrackets = []
        for a, b in enumerate(s):
            if b == '(' or b == '[' or b == '{':
                stackLeftBrackets.append(b)
            else:
                if not stackLeftBrackets \
                or (stackLeftBrackets[-1] == '(' and b != ')') \
                or (stackLeftBrackets[-1] == '[' and b != ']') \
                or (stackLeftBrackets[-1] == '{' and b != '}'):
                    return False
                else:
                	del stackLeftBrackets[-1]
                    
        return stackLeftBrackets == []
        # if stackLeftBrackets:
        #     return False
        # else:
        #     return True

def main():
    # True
    s1 = "()[]{}"
    # False
    s2 = "({)]{}"
    # True
    s3 = "([{}])"
    # True
    s4 = "(((({[]}))))"
    # False
    s5 = "((({[]}))))"
    # False
    s6 = "((({[]}))"
    test = Solution()
    print(test.isValid(s1))
    print(test.isValid(s2))
    print(test.isValid(s3))
    print(test.isValid(s4))
    print(test.isValid(s5))
    print(test.isValid(s6))


if __name__ == '__main__':
    main()
