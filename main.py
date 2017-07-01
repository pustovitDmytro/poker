
#C=Clubs, D=Diamonds, H=Hearts, S=Spades
SUITS = ["C","D","H","S"]
#A=Ace, 2-9, T=10, J=Jack, Q=Queen, K=King
FACES = range(2,15)

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
    if arr[-1]['face']==FACES[-1]:
        aces = list(filter(lambda x: x['face']==FACES[-1],cards))
        minAce = sorted(aces, key=lambda x: x['position'])[0]
        combination = [minAce]
        old = 1
    else:
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
        if len(combination)>=5:
            print(combination)
            combination = sorted(combination,key=lambda x: x['position'])
            result = fit(combToInt(combination[:5]))
            if result:
                return True
    return False

def straight_flush(cards):
    for suit in SUITS:
        suited = list(filter(lambda x: x['suit']==suit,cards))
        if len(suited)>4:
            result = straight(suited)
            if result:
                return True
    return False

def flush(cards):
    for suit in SUITS:
        suited = list(filter(lambda x: x['suit']==suit,cards))
        suited = sorted(suited,key=lambda x: x['position'])
        if len(suited)>=5:
            combination = suited[:5]
            result = fit(combToInt(combination))
            if result:
                return True
    return False

def n_of_a_kind(n, cards):
    for face in FACES:
        faced = list(filter(lambda x: x['face']==face,cards))
        faced = sorted(faced,key=lambda x: x['position'])
        if len(faced) >= n:
            combination = faced[:n]
            result = fit(combToInt(combination))
            if result:
                print(combination)
                return True
    return False

def n_m_of_a_kind(n,m,cards):
    variants = {"left": [], "right": []}
    combination = []
    for face in range(2, 15):
        faced = list(filter(lambda x: x['face'] == face, cards))
        faced = sorted(faced, key=lambda x: x['position'])
        if len(faced) >= n: variants['right'].append({'face': face, 'arr': faced[:n]})
        if len(faced) >= m: variants['left'].append({'face': face, 'arr': faced[:m]})
    for right in variants["right"]:
        for left in variants["left"]:
            if left['face'] != right['face']:
                combination = left['arr']+right['arr']
                result = fit(combToInt(combination))
                if result:
                    return True
    return False


def fit(comb):
    if len(comb)>5|len(comb)<1:
        return False
    desk=list(filter(lambda x: x>4,comb))
    if len(desk)<1:
        return True
    desk.sort()
    handOut = 5 - (len(comb)- len(desk))
    deskLast=desk[-1]
    print(comb,handOut,deskLast)
    if handOut>=deskLast-4:
        return True
    else:
        return False

def combToInt(combination):
    return [item['position'] for item in combination]

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

rules = [
    {
        'value':9,
        'message':"straight-flush",
        'method': straight_flush
    },
    {
        'value':8,
        'message':"four-of-a-kind",
        'method': lambda x: n_of_a_kind(4, x)
    },
    {
        'value':7,
        'message':"full-house",
        'method': lambda x: n_m_of_a_kind(2,3,x)
    },
    {
        'value':6,
        'message':"flush",
        'method':flush
    },
    {
        'value':5,
        'message':"straight",
        'method':straight
    },
    {
        'value':4,
        'message':"three-of-a-kind",
        'method':lambda x: n_of_a_kind(3, x)
    },
    {
        'value':3,
        'message':"two-pairs",
        'method': lambda x: n_m_of_a_kind(2,2,x)
    },
    {
        'value':2,
        'message':"one-pair",
        'method':lambda x: n_of_a_kind(2, x)
    },
    {
        'value':1,
        'message':"highest-card",
        'method':lambda x: n_of_a_kind(1, x)
    }
]

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
    order = sorted(rules, key=lambda x: x['value'], reverse=True)
    message = ''
    for check in order:
        print(check['message'])
        if check['method'](cards):
            message = check['message']
            break
    outline+=message+'\n'
    print(outline)
    putLineToFile("out.txt",outline)