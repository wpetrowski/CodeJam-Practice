# https://code.google.com/codejam/contest/1277486/dashboard

import sys

N = int(sys.stdin.readline())

vowels = 'aeiou'

for i in xrange(N):
    expr = sys.stdin.readline().strip()
    d = {}

    for start in xrange(len(expr)-1):
        for end in xrange(start+1, len(expr)):
            sub = expr[start:end]

            c = len(filter(lambda x: x in "aeiou", sub))

            if c == 1:
                if not sub in d:
                    d[sub] = []
                d[sub].append(start)

            elif c > 1:
                break

    print 'Case #%d:' % (i+1)
    print expr
    print sorted(d.items(), key=lambda x: x[1])
