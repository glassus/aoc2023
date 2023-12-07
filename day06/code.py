races = [(61, 643), (70, 1184), (90, 1362), (66, 1041)]
#races = [(7, 9), (15, 40), (30, 200)]

def hold_to_dist(t, time_race):
    return t * (time_race - t)

def nb_wins(race):
    time_race, record = race
    nb = 0
    for t in range(time_race+1):
        if hold_to_dist(t, time_race) > record:
            nb += 1
    return nb

def part1():
    s = 1
    for race in races:
        s = s * nb_wins(race)
    return s

def part2():
     return nb_wins((61709066, 643118413621041))
    
    
def formule(race):
    T, dmax = race
    return (T**2 - 4*dmax)**0.5

for race in races:
    print(formule(race))