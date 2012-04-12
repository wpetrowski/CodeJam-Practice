# https://code.google.com/codejam/contest/1277486/dashboard

import sys

def findShortUniqueSubstr(item, songs):
    songs.remove(item)
    startPos = 0
    minLen = len(item) + 1
    minStr = ":("

    while startPos < len(item):
        endPos = startPos
        curLen = endPos - startPos
        while endPos <= len(item) and curLen <= minLen:
            curLen = endPos - startPos
            curStr = item[startPos:endPos]
            if (not isStrInList(curStr, songs)):
                if minStr == ":(" or curLen < minLen or (curLen == minLen and curStr < minStr):
                    minLen = curLen
                    minStr = curStr
            endPos += 1
        startPos += 1
    if minStr != ":(":
        minStr = '"%s"' % minStr
    return minStr

def isStrInList(str, list):
    for item in list:
        if str in item:
            return True
    return False

N = int(sys.stdin.readline())

for i in xrange(N):
    numSongs = int(sys.stdin.readline())
    print 'Case #%d:' % (i+1)
    songs = []

    for j in xrange(numSongs):
        songs.append(sys.stdin.readline().strip().upper())

    for song in songs:
        print findShortUniqueSubstr(song, songs[:])


