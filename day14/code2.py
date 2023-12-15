data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

d = {}
hauteur = len(data)
largeur = len(data[0])
for i in range(len(data)):
    for k in range(len(data[0])):
        pos = k - i*1j
        d[pos] = data[i][k]
for k in range(-1, largeur+1):
    d[k + 1j] = '#'
    d[k - hauteur*1j] = '#'
for i in range(-1, hauteur+1):
    d[-1 - i*1j] = '#'
    d[largeur - i*1j] = '#'





def bouge(pos, dir):
    if d[pos + dir] in ("#","O"):
        return None
    d[pos] = '.'
    pos = pos + dir
    while d[pos] not in ("#","O"):
        pos = pos + dir
    pos = pos - dir
    d[pos] = "O"

def affiche():
    for i in range(-1, len(data)+1):
        s = ""
        for k in range(-1, len(data[0])+1):
            s += d[k - i*1j]
        print(s)

def bouge_all(direction):
    parcNS = list(range(len(data)))
    parcSN = parcNS[::-1]
    parcWE = range(len(data[0]))
    parcEW = parcWE[::-1]
    
    if direction == 'N':
        dir = 1j
        for i in parcNS:
            for k in parcWE:
                pos = k - i*1j
                if d[pos] == 'O':
                    bouge(pos, dir)
    if direction == 'S':
        dir = -1j
        for i in parcSN:
            for k in parcWE:
                pos = k - i*1j
                if d[pos] == 'O':
                    bouge(pos, dir)                    
    if direction == 'W':
        dir = -1
        for i in parcSN:
            for k in parcWE:
                pos = k - i*1j
                if d[pos] == 'O':
                    bouge(pos, dir)                      
    if direction == 'E':
        dir = 1
        for i in parcSN:
            for k in parcEW:
                pos = k - i*1j
                if d[pos] == 'O':
                    bouge(pos, dir)                    

def total_load():
    s = 0
    for i in range(len(data)):
        for k in range(len(data[0])):
            pos = k - i*1j
            if d[pos] == 'O':
                load = len(data) + int(pos.imag)
                s += load
    return s

n = 5000
mem1 = []
mem2 = []
per = 65
for k in range(n):
    for dir in ('N', 'W', 'S', 'E'):
        bouge_all(dir)
    v = total_load()
    i = k % 1000
    if 0 <= i < per:
        #print("------------")
        mem1.append(v)
        #print(mem1)
    if per <= i < 2*per:
        mem2.append(v)
    #print(mem1, mem2)
    if len(mem2) == per:
        
        if mem1 == mem2:
            print("fini")
            print(k+1, mem1)
            val = k+1
            break
        else:
            mem1 = []
            mem2 = []
    #print(k, v)
a = (10**9 - val) % per
print(mem1[a-1])
