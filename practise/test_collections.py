<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


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
=======
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
>>>>>>> 1e8bf7e351d17dae0c5ac95fe4e6512702d14e0b
