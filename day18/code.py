data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
from collections import defaultdict


minX, maxX, minY, maxY = 0, 0, 0, 0

def parse(line):
    a = line.split(' ')
    return a[0], int(a[1]), a[2]

def parse2(line):
    a = line.split(' ')
    h = a[2][2:-1]
    val = int(h[:-1], 16)
    dir = int(h[-1])
    direc = {0:'R', 1:'D', 2:'L', 3:'U'}[dir]
    return direc, val, 2



moves = [parse(line) for line in data]
d = defaultdict(str)

def trace(moves):
    global minX, maxX, minY, maxY
    direct = {'U':1j, 'D':-1j, 'L':-1, 'R':1}
    pos = 0
    d[pos] = '#'
    
    for move in moves:
        dir, val, col = move
        for _ in range(val):
            pos += direct[dir]
            d[pos] = '#'
            x, y = int(pos.real), int(pos.imag)
            minX = min(minX, x)
            minY = min(minY, y)            
            maxX = max(maxX, x)
            maxY = max(maxY, y)             
trace(moves)


def diffuse(pos):
    if d[pos] == '#':
        return None
    file = [pos]
    while file:
        curr = file.pop(0)
        for dep in [1,-1,1j,-1j]:
            newpos = curr + dep
            if d[newpos] not in ('#', 'P'):
                d[newpos] = 'P'
                file.append(newpos)
        



def compte(line):
    i = 0
    n = 0
    inside = False
    while i < len(line):
        v = 0
        while i < len(line) and line[i] == '.':
            i += 1
            if inside:
                v += 1
        if i < len(line):        
            n += v
        inside = not inside
        while i < len(line) and line[i] == '#':
            i += 1
            #n += 1
    return n 
 
def affiche():
    n = 0
    f = open('map.txt', 'w') 
    for k in range(-minY+2, -maxY-3, -1):
        s = ''
        for i in range(minX-1, maxX+2):
            pos = i - k*1j
            if pos in d:
                s += str(d[pos])
            else:
                s += '.'      
        f.write(s + '\n')
        #n += compte(s)
    f.close()
    return n


print(affiche())











# d = {}
# for i in range(len(data)):
#     for k in range(len(data[0])):
#         pos = k - i*1j
#         d[pos] = int(data[i][k])
# 
# H = len(data)
# W = len(data[0])



