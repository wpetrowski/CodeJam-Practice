# https://code.google.com/codejam/contest/1277486/dashboard

def whisperTo(i, monks, followers):
    w = monks[i]
    monks[i] = 1
    if not w:
        return followers[i]
    return []

import sys

T = int(sys.stdin.readline())

for case in xrange(1, T+1):
    N = int(sys.stdin.readline())
    follows = [int(x) for x in sys.stdin.readline().split()]
    assert len(follows) == N, "input error!"

    # convert from follows to followers
    followers = [[] for x in range(N)]
    for i in xrange(N):
        followers[follows[i] - 1].append(i)

    print "Case #%d:" % case

    for day in xrange(N):
        monks = [0 for x in range(N)]
        todo = [day]
        while len(todo) > 0:
            todo.extend(whisperTo(todo.pop(0), monks, followers))
        print sum(monks)


