import binHex

sqWid = 13
sqsWide = 5

def repeat(x, n):
    return n*x

rowDiv = [repeat('-', sqWid) for i in range(sqsWide)]
rowDwn = [repeat('X', sqWid) for i in range(sqsWide)]
rowUp = [repeat(' ', sqWid) for i in range(sqsWide)]

def labelDown(label):
    return '{:X^13}'.format(' ' + label + ' ')

def labelUp(label):
    return '{:^13}'.format(' ' + label + ' ')

def row(labels, div, w, n):
    return div+div.join(labels)+div

r0 = [x[2] for x in binHex.binHexNums()[:5]]
r1 = [x[2] for x in binHex.binHexNums()[5:10]]
r2 = [x[2] for x in binHex.binHexNums()[10:15]]
r3 = [x[2] for x in binHex.binHexNums()[15:20]]
r4 = [x[2] for x in binHex.binHexNums()[20:25]]

def printRow(r):
    print(row(rowDiv, "+", 13, 5))
    print(row(rowUp, "|", 13, 5))
    print(row(rowUp, "|", 13, 5))
    print(row(list(map(labelUp, r)), '|', sqWid, sqsWide))
    print(row(rowUp, "|", 13, 5))
    print(row(rowUp, "|", 13, 5))

def printBoard():
    printRow(r0)
    printRow(r1)
    printRow(r2)
    printRow(r3)
    printRow(r4)
    print(row(rowDiv, "+", 13, 5))

printBoard()