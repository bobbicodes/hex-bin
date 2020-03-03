import binHex

sqWid = 12
sqsWide = 5

def repeat(x, n):
    return n*x

rowDwn = [repeat('X', sqWid) for i in range(sqsWide)]
rowUp = [repeat(' ', sqWid) for i in range(sqsWide)]

def labelDown(label):
    return '{:X^12}'.format(' ' + label + ' ')

def labelUp(label):
    return '{:^12}'.format(' ' + label + ' ')

def row(labels, div, w, n):
    return div+div.join(labels)+div

r0 = [x[2] for x in binHex.binHexNums()[:5]]
r1 = [x[2] for x in binHex.binHexNums()[5:10]]
r2 = [x[2] for x in binHex.binHexNums()[10:15]]
r3 = [x[2] for x in binHex.binHexNums()[15:20]]
r4 = [x[2] for x in binHex.binHexNums()[20:25]]

#print(row("-", "+", 12, 5))
#print(row("X", "|", 12, 5))
#print(row("X", "|", 12, 5))
print(row(list(map(labelUp, r0)), '|', sqWid, sqsWide))