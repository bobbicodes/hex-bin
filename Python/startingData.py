from random import randint

def squares(rows):
    sqList = []
    n = 0
    for l in range(rows):
        for m in range(rows):
            sqList.append((n, str(l) + str(m)))
            n +=1
    return sqList
  
#print(squares(5))

def shuffle(l):
    count = 0
    randomList = []
    for i in range(0, (len(l))):
        number = randint(0, (len(l)-1))
        randomList.append(l.pop(number))
        count +=1
    return randomList

randomBoxStringTupleList = shuffle(squares(5))

def binHexNums():
    hexList = []
    binList = []
    binHexList = []
    aList = []
    hexString = '0x'
    secondDigit = ['0', 'a', 'f']
    num = 0
    count = 0

    for j in range(len(secondDigit)):
        for i in range(16):
            firstDigit = str(hex(i))
            firstDigit = firstDigit[-1]
            hexList.append(hexString + secondDigit[j] + firstDigit)
            if secondDigit[j] == 'a' or secondDigit[j] == 'A':
                num = 160
            elif secondDigit[j] == 'b' or secondDigit[j] == 'B':
                num = 176
            elif secondDigit[j] == 'c' or secondDigit[j] == 'C':
                num = 192
            elif secondDigit[j] == 'd' or secondDigit[j] == 'D':
                num = 208
            elif secondDigit[j] == 'e' or secondDigit[j] == 'E':
                num = 224
            elif secondDigit[j] == 'f' or secondDigit[j] == 'F':
                num = 240
            else:
                num = 16*int(secondDigit[j])
            number = num + i
     
            if secondDigit[j] == '0':
                binString = bin(number)
                while len(binString) != 6:
                    binString = binString[:2] + '0' + binString[2:]
                binaryNum = '0b0000 ' + binString[2:]
            else:
                binaryNum = bin(number)
                binaryNum = binaryNum[:6] + ' ' + binaryNum[6:]
            binList.append(binaryNum)
            aList.append([hexList[j*16 + i], binList[j* 16 + i], number])
            binHexList.append(aList[count])
            count +=1
    #pick twelve pairs for the board
    nextList = []
    for i in range(12):
        randNumber = randint(0, (len(binHexList)-1))
        nextList.append(binHexList.pop(randNumber))

    # now add WildCard
    wildCardNum = randint(0, 23)
    finalTupleList = []
    counter = 0
    done = 0
    for i in range(12):
        if i == int(wildCardNum/2) and done == 0 or i == (int(wildCardNum/2) + 1) and done == 0:
            finalTupleList.append((randomBoxStringTupleList[counter][0], randomBoxStringTupleList[counter][1], 'Wild Card', 1000))
        
            counter +=1
            done = 1
        finalTupleList.append((randomBoxStringTupleList[counter][0], randomBoxStringTupleList[counter][1], nextList[i][0], nextList[i][2]))
        counter +=1
        finalTupleList.append((randomBoxStringTupleList[counter][0], randomBoxStringTupleList[counter][1], nextList[i][1], nextList[i][2]))
        counter +=1
    finalTupleList.sort()
    return finalTupleList
          
print(binHexNums())