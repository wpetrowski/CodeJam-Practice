# https://code.google.com/codejam/contest/1277486/dashboard

import sys

def checkIfSpell(word, start_ix, end_ix, orig_end_ix, curSyl, repeatedSyllables, numSyls):
    if start_ix + len(curSyl) >= orig_end_ix:
        return False

    inner = word[start_ix+len(curSyl):orig_end_ix]
    if len(inner) == 0:
        return False

    if len(filter(lambda x: x in "aeiou", inner)) > 0 and numSyls > 1:
        return True

    new_start = start_ix + len(curSyl)
    new_end = end_ix + len(curSyl)

    #find another repeated syllable that has instances at start + len and end + len
    for newSyl in filter(lambda x: new_start in x[1] and new_end in x[1], repeatedSyllables):
        if checkIfSpell(word, new_start, new_end, orig_end_ix, newSyl[0], repeatedSyllables, numSyls+1):
            return True
    return False

N = int(sys.stdin.readline())

for i in xrange(N):
    expr = sys.stdin.readline().strip()
    d = {}

    for start in xrange(len(expr)-1):
        for end in xrange(start+1, len(expr)+1):
            sub = expr[start:end]

            c = len(filter(lambda x: x in "aeiou", sub))

            if c == 1:
                if not sub in d:
                    d[sub] = []
                d[sub].append(start)

            elif c > 1:
                break

    repeatedSyllables = filter(lambda x: len(x[1]) > 1, d.items())

    found = False
    for syl in repeatedSyllables:
        if found:
            break
        for i in xrange(len(syl[1]) - 1):
            if found:
                break
            for j in xrange(i+1, len(syl[1])):
                if found:
                    break
                start_ix = syl[1][i]
                end_ix = syl[1][j]
                numSyls = 1

                found = checkIfSpell(expr, start_ix, end_ix, end_ix, syl[0], repeatedSyllables, numSyls)

    print 'Case #%d:' % (i+1)
    print expr
    print found
    #print sorted(d.items(), key=lambda x: x[1])
    #print sorted(repeatedSyllables, key=lambda x: x[1])
