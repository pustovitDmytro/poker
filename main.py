"""straight-flush
four-of-a-kind
full-house
flush
straight
three-of-a-kind
two - pairs
one-pair
highest-card"""
#C=Clubs, D=Diamonds, H=Hearts, S=Spades
SUITS = ["C","D","H","S"]
#A=Ace, 2-9, T=10, J=Jack, Q=Queen, K=King
def faceToInt(face):
    if face == "A":
        return 14
    elif face=="K":
        return 13
    elif face=="Q":
        return 12
    elif face=="J":
        return 11
    elif face=="T":
        return 10
    else: return int(face)

def straight(cards):
    arr = sorted(cards,key=lambda x: x['face'])
    combination = []
    old = 0
    for card in arr:
        current = card['face']
        if current-old > 1:
            combination = [card]
        elif current-old==1:
            combination.append(card)
        else: pass
        old=current
        if len(combination)==5:
            return combination
    return []

def straight_flush(cards):
    for suit in SUITS:
        suited = list(filter(lambda x: x['suit']==suit,cards))
        if len(suited)>4:
            combination = straight(suited)
            if combination:
                print("straight_flush")
                return combination
    return []

def flush(cards):
    for suit in SUITS:
        suited = list(filter(lambda x: x['suit']==suit,cards))
        if len(suited)>4:
            print("flush")

def n_of_a_kind(cards,n):
    for face in range(2,15):
        faced = list(filter(lambda x: x['face']==face,cards))
        faced = sorted(faced,key=lambda x: x['position'])
        if len(faced) >= n:
            faced[:n]
            print(n,"_of_a_kind")

def n_m_of_a_kind(cards,n,m):
    variants = {"three": [], "two": []}
    combination = []
    for face in range(2, 15):
        faced = list(filter(lambda x: x['face'] == face, cards))
        faced = sorted(faced, key=lambda x: x['position'])
        if len(faced) >= n: variants['two'].append({'face': face, 'arr': faced[:n]})
        if len(faced) >= m: variants['three'].append({'face': face, 'arr': faced[:m]})
    for right in variants["two"]:
        for left in variants["three"]:
            if left['face'] != right['face']:
                print("n_m_house",n,m)

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
        'face':faceToInt(str[0]),
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


    straight_flush(cards)
    n_of_a_kind(cards,4)
    n_m_of_a_kind(cards,2,3)
    flush(cards)
    straight(cards)
    n_of_a_kind(cards,3)
    n_m_of_a_kind(cards, 2, 2)
    n_of_a_kind(cards, 2)
    n_of_a_kind(cards, 1)


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