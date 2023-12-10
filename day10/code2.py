data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

d = {}
new = {}
for i in range(len(data)):
    for k in range(len(data[0])):
        pos = k - i*1j
        d[pos] = data[i][k]
        new[pos] = '.'
        if d[pos] == 'S':
            start = pos
            

pos = start 
let = 'D'
dir = 1
n = 0
while let != 'S':
    
    pos = pos + dir
    let = d[pos]
    new[pos] = 'X'
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


pos = start 
let = 'D'
dir = 1
n = 0
while let != 'S':
    prev_pos = pos
    pos = pos + dir
    let = d[pos]
    #new[pos] = 'X'
    
    dir_trace = dir * 1j
    pos_trace = pos + dir_trace
    while new[pos_trace] != 'X':
        new[pos_trace] = 'I'
        pos_trace += dir_trace
    
    dir_trace = dir * 1j
    prev_pos_trace = prev_pos + dir_trace
    while new[prev_pos_trace] != 'X':
        new[prev_pos_trace] = 'I'
        prev_pos_trace += dir_trace


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




def affiche():
    with open("newmap.txt", 'w') as f:
        for i in range(len(data)):
            s = ''
            for k in range(len(data[0])):
                s += new[k - i*1j]
            f.write(s)
            f.write('\n')

affiche()
print(sum(new[k] == 'I' for k in new))