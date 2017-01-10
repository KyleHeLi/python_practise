#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import re


def checkEmail(string):
    re_mail = re.compile(r'^([a-zA-Z0-9\.\_\-]+@[a-zA-Z0-9]+\.[0-9a-zA-Z]+)$')
    nList = re.split(r'[\s]+', string)
    if len(nList) < 2:
        # For example 1 and 2
        return re_mail.match(string).group(0)
    else:
        # For exmaple 3
        return nList[-1]


def main():
    text = 'a b   c'
    text1 = 'a, b,   c d'
    text2 = 'a, b;;   c d'
    s = r'ABC\-001'

    print text.split(' ')
    print re.split(r'\s+', text)
    print re.split(r'[\s\,]+', text1)
    print re.split(r'[\s\,\;]+', text2)

    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print("=============")
    print m
    print m.group(0)
    print m.group(1)
    print m.group(2)

    t = '19:05:30'
    m = re.match(
        r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
    print m.groups()

    # Default is greedy match
    print re.match(r'^(\d+)(0*)$', '102300').groups()

    # Use non-greedy match
    print re.match(r'^(\d+?)(0*)$', '102300').groups()

    # Check the email address
    e1 = "someone@gmail.com"  # r'someone@gmail.com'
    e2 = "bill.gate@microsoft.com"  # r'bill.gate@microsoft.com'
    e3 = "lv-bmw@163.com"  # r'lv-bmw@163.com'
    e4 = "god_life@uottawa.ca"  # r'god_life@uottawa.ca'
    e5 = "<Tom Paris> tom@voyager.org"
    print checkEmail(e1)
    print checkEmail(e2)
    print checkEmail(e3)
    print checkEmail(e4)
    print checkEmail(e5)


if __name__ == '__main__':
    main()
