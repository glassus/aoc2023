data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

d = {}
for i in range(len(data)):
    for k in range(len(data[0])):
        pos = k - i*1j
        d[pos] = data[i][k]
        
def remonte(pos):
    if pos.imag == 0:
        return None
    if d[pos + 1j] in ("#","O"):
        return None
    d[pos] = '.'
    pos = pos + 1j
    while d[pos] not in ("#","O") and pos.imag <= 0:
        pos = pos + 1j
        if pos.imag == 1:
            break
    pos = pos - 1j
    d[pos] = "O"

def affiche():
    for i in range(len(data)):
        s = ""
        for k in range(len(data[0])):
            s += d[k - i*1j]
        print(s)

def remonte_all():
    for i in range(len(data)):
        for k in range(len(data[0])):
            pos = k - i*1j
            if d[pos] == 'O':
                remonte(pos)

def total_load():
    s = 0
    for i in range(len(data)):
        for k in range(len(data[0])):
            pos = k - i*1j
            if d[pos] == 'O':
                load = len(data) + int(pos.imag)
                s += load
    return s
    