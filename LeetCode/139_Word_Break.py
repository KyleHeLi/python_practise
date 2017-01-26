#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict:
         List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        d = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if word == s[i - len(word) + 1:i + 1] and (d[i - len(word)] or i - len(word) == -1):
                    d[i] = True
        return d[-1]

    def wordBreak1(self, s, words):
        ok = [True]
        for i in range(1, len(s) + 1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]


def main():
    testStr0 = "leetcode"
    testDict0 = ['leet', 'code', 'good']

    testStr = "gooday"
    testStr2 = "goodbye"
    testStr3 = "goodday"
    testDict = ['good', 'day']
    testDict2 = ['good']
    test = Solution()

    print test.wordBreak(testStr0, testDict0)
    print("================")
    print test.wordBreak(testStr, testDict)
    print test.wordBreak(testStr2, testDict)
    print test.wordBreak(testStr3, testDict)
    print("================")
    print test.wordBreak(testStr, testDict2)
    print test.wordBreak(testStr2, testDict2)
    print test.wordBreak(testStr3, testDict2)


if __name__ == '__main__':
    main()
