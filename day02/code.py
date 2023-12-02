data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

def parse_game(line):
    a = line.split(': ')
    nb = int(a[0].split(' ')[1])
    tir = a[1].split('; ')
    return nb, tir

class Game:
    def __init__(self, nb, tir):
        self.nb = nb
        self.tirages = self.affecte_tir(tir)
        
    def affecte_tir(self, tir):
        s = []
        for tirage in tir:
            d = {'red':0, 'green':0, 'blue':0}
            balls = tirage.split(', ')
            for t in balls:
                n, col = t.split(' ')
                d[col] += int(n)
            s.append(d)
        return s
            
games = [Game(*parse_game(line)) for line in data]


def is_possible(game):
    maxi = {"red":12, "green":13, "blue":14}
    for d in game.tirages:
        if any(d[color] > maxi[color] for color in maxi):
            return False
    return True

def part1():
    return sum(game.nb for game in games if is_possible(game))

def power(game):
    maxi = {"red":0, "green":0, "blue":0}
    for d in game.tirages:
        for color in maxi:
            if d[color] > maxi[color]:
                maxi[color] = d[color]
    return maxi["red"]*maxi["green"]*maxi["blue"]

def part2():
    return sum(power(game) for game in games)    
    