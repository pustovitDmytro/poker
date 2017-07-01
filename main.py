"""straight-flush
four-of-a-kind
full-house
flush
straight
three-of-a-kind
two - pairs
one-pair
highest-card"""


def fit(comb):
    if len(comb)>5|len(comb)<1:
        return False
    desk=list(filter(lambda x: x>5,comb))
    desk.sort()
    handOut = 5 - (len(comb)- len(desk))
    deskLast=desk[-1]
    print(handOut,deskLast)
    if handOut>deskLast-5:
        return True
    else:
        return False

def getLineFromFile(way,pos=0):
    f = open(way,'rU')
    f.seek(pos)
    line = f.readline()
    nextPos = f.tell()
    if not line: nextPos = -1
    f.close()
    return(nextPos,line)
def putLineToFile(way,line):
    f = open(way,'a')
    f.writelines(line)
    f.close()
def clearFile(way):
    f = open("out.txt", 'w')
    f.truncate(0)
    f.close()


def strToCard(str,position):
    obj = {
        'face':str[0],
        'suit':str[1],
        'position':position
    }
    return obj

position=0
clearFile("out.txt")
while True:
    (position,line) = getLineFromFile("test.txt",position)
    if position<0:
        break
    strCards = line.replace('\n','').split(' ')
    cards = []
    for i,strCard in enumerate(strCards):
        cards.append(strToCard(strCard,i))
    print(cards)
    outline = "Hand: "
    for i in range(5):
        outline+=strCards[i]+" "
    outline+="Deck: "
    for i in range(5,10):
        outline+=strCards[i]+" "
    outline+="Best hand: "
    outline+='\n'
    print(outline)
    putLineToFile("out.txt",outline)