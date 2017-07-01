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






fit([1,5,8,9,4])