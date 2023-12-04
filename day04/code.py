data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

def parse(line):
    a = line.split(':')
    b = a[0].split()
    idx = int(b[-1])
    c = a[1].split(' | ')
    wins = [k for k in c[0].split()]
    wins = [int(k) for k in wins]
    numbers = [k for k in c[1].split()]
    numbers = [int(k) for k in numbers]
    return idx, wins, numbers


class Card:
    def __init__(self, idx, wins, numbers):
        self.idx = idx
        self.wins = wins
        self.numbers = numbers
        self.nb_matching_numbers = len(set(self.wins).intersection(set(self.numbers)))
        self.exemplaires = 1

    def points(self):
        p = 2**(-1 + self.nb_matching_numbers)
        if p == 0.5:
            p = 0
        return p
    
cards = [Card(*parse(line)) for line in data]

def part1():
    return sum(card.points() for card in cards)

        
def part2():
    for i in range(len(cards)):
        nb_copys = cards[i].nb_matching_numbers
        for k in range(1, nb_copys + 1):
            cards[i+k].exemplaires += cards[i].exemplaires
    return sum(card.exemplaires for card in cards)
