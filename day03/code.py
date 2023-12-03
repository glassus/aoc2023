data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

width = len(data[0])
height = len(data)

stars = {}

for i in range(height):
    for j in range(width):
        if data[i][j] == '*':
            stars[(i,j)] = []


def voisins(pos):
    x, y = pos
    lst = []
    d = [(-1,0), (1,0), (0,-1), (0,1)]
    diag = [(-1,-1), (-1,1), (1,-1), (1,1)]
    d = d + diag
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if (0 <= nx < width)  and  (0 <= ny < height):
            lst.append((nx, ny))
    return lst

def is_number(pos):
    i, j = pos
    return data[i][j].isdigit()

def is_symbol(pos):
    i, j = pos
    return (not data[i][j].isdigit()) and (not data[i][j] == '.')

def parcours(i):
    nb = []
    s = ''
    valid = False
    linked_stars = []
    for j in range(width):
        if is_number((i,j)):
            for vi, vj in voisins((i,j)):
                if (vi,vj) in stars:
                    linked_stars.append((vi,vj))
                if is_symbol((vi, vj)):
                    valid = True
            if s == '':
                s = data[i][j]
            else:
                s += data[i][j]
        if data[i][j] == '.' or j == width-1 or is_symbol((i,j)):
            if s != '' and valid:
                val = int(s)
                nb.append(val)
                for pos in linked_stars:
                    if val not in stars[pos]:
                        stars[pos].append(val)
            s = ''
            valid = False
            linked_stars = []


    return nb

def part1():
    s = 0
    for i in range(height):
        s += sum(parcours(i))
    return s


def part2():
    for i in range(height):
        parcours(i)
    s = 0
    for pos in stars:
        lst = stars[pos]
        if len(lst) == 2:
            s += lst[0]*lst[1]
    return s
