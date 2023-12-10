data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

d = {}
for i in range(len(data)):
    for k in range(len(data[0])):
        pos = k - i*1j
        d[pos] = data[i][k]
        if d[pos] == 'S':
            start = pos
            

pos = start 
let = 'D'
dir = 1
n = 0
while let != 'S':
    
    pos = pos + dir
    let = d[pos]
    if let == 'J':
        if dir == 1:
            dir = 1j
        else:
            dir = -1
    if let == '7':
        if dir == 1:
            dir = -1j
        else:
            dir = -1
    if let == 'F':
        if dir == 1j:
            dir = 1
        else:
            dir = -1j
    if let == 'L':
        if dir == -1j:
            dir = 1
        else:
            dir = 1j
    n += 1