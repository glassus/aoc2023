data = open('input.txt').read().splitlines()[0]
#data = open('input_test.txt').read().splitlines()[0]

lst = data.split(',')

def algo(car, curr):
    curr = (17* (curr + ord(car))) % 256
    return curr
    
def alg_hash(word):
    curr = 0
    for car in word:
        curr = algo(car, curr)
    return curr

def part1():
    return sum(alg_hash(word) for word in lst)

box = [[] for _ in range(256)]

def action(inst):
    if '=' in inst:
        f = inst.split('=')
        name = f[0]
        focal = int(f[1])
        nb_box = alg_hash(name)
        present = False
        for i in range(len(box[nb_box])):
            lens, _ = box[nb_box][i]
            if lens == name:
                present = True
                box[nb_box][i] = [name, focal]
        if present == False:
            box[nb_box].append([name, focal])
    if '-' in inst:
        name = inst[:-1]
        nb_box = alg_hash(name)
        to_remove = None
        for i in range(len(box[nb_box])):
            lens, _ = box[nb_box][i]
            if lens == name:
                to_remove = i
        if to_remove is not None:
            del box[nb_box][to_remove]
            
        
for inst in lst:
    action(inst)
    
s = 0       
for i in range(len(box)):
    for k in range(len(box[i])):
        v = box[i][k][1]
        s += (i+1)*(k+1)*v
print(s)