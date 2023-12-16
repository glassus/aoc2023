data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

d = {}
for i in range(len(data)):
    for k in range(len(data[0])):
        pos = k - i*1j
        d[pos] = data[i][k]

W = len(data[0])
H = len(data)

r = {}
passage = {}

def is_inside(pos):
    x = pos.real
    y = pos.imag
    return 0 <= x < W and -H < y <= 0

def trace(pos, direction):
    if pos in passage:
        if passage[pos] == direction:
            return None
    else:
        passage[pos] = direction
        
    r[pos] = '#'
    pos += direction
    
    while is_inside(pos) and d[pos] == '.':
        r[pos] = '#'
        pos += direction

    if is_inside(pos) and d[pos] == '|':
        if direction in (1, -1):
            trace(pos, 1j)
            trace(pos, -1j)
        else:
            r[pos] = '#'
            #pos += direction
            trace(pos, direction)
    elif is_inside(pos) and d[pos] == '-':
        if direction in (1j, -1j):
            trace(pos, 1)
            trace(pos, -1)
        else:
            r[pos] = '#'
            #pos += direction
            trace(pos, direction)
    elif is_inside(pos) and d[pos] == '\\':
        if direction in (1, -1):
            trace(pos, direction * (-1j))
        if direction in (1j, -1j):
            trace(pos, direction * 1j)
    elif is_inside(pos) and d[pos] == '/':
        if direction in (1, -1):
            trace(pos, direction * 1j)
        if direction in (1j, -1j):
            trace(pos, direction * (-1j))

def affiche():
    for i in range(len(data)):
        s = ''
        for k in range(len(data[0])):
            pos = k - i*1j
            if pos in r:
                s += '#'
            else:
                s += '.'
        print(s)

trace(-1-3j,1)
#affiche()
print(len(r)-1)