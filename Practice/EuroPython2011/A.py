# https://code.google.com/codejam/contest/1277486/dashboard

import sys

N = int(sys.stdin.readline())

for i in xrange(N):
    line = sys.stdin.readline().strip()
    print 'Case #%d: %s is ruled by' % (i+1, line),
    if line.lower().endswith(('a', 'e', 'i', 'o', 'u')):
        print 'a queen.'
    elif line.lower().endswith('y'):
        print 'nobody.'
    else:
        print 'a king.'
