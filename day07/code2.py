data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
from itertools import combinations_with_replacement

points = {}
for line in data:
    k = line.split()
    points[k[0]] = int(k[1])

hands = list(points.keys())

def make_dict(hand):
    d = {}
    for c in hand:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d



def val_hand(hand):
    d = make_dict(hand)
    if len(d) == 1:
        return 0
    if len(d) == 2:
        if max(d.values()) == 4:
            return 1
        return 2
    if len(d) == 3:
        if max(d.values()) == 3:
            return 3
        return 4
    if len(d) == 4:
        return 5
    return 6

def rank_tie(card):
    alph = {'A':'a', 'K':'b', 'Q':'c', 'J':'n',\
            'T':'e', '9':'f', '8':'g', '7':'h',\
            '6':'i', '5':'j', '4':'k', '3':'l', '2':'m'}
    return "".join(alph[k] for k in card)


def new_val_hand(hand):
    if 'J' not in hand:
        return val_hand(hand)
    others = [k for k in hand if k != 'J']
    if len(others) == 0:
        return 0
    gen = set(others)
    nb_new = 5 - len(others)
    mini = 8
    for to_add in combinations_with_replacement(gen, r=nb_new):
        new_hand = "".join(list(to_add) + others)
        v = val_hand(new_hand)
        if v < mini:
            mini = v
    return mini



hands = sorted(hands, key= lambda x: (new_val_hand(x), rank_tie(x)))

def total_winnings(hands):
    s = 0
    for i in range(len(hands)):
        s += points[hands[i]] * (len(hands)-i)
    return s