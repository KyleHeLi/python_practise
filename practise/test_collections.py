#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict


def main():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print p.x
    print p.y

    print("========")
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')
    print q

    print("========")
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print dd['key1']
    print dd['key2']

    print("========")
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print d
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print od


if __name__ == '__main__':
    main()
