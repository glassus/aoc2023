data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

inst = data[0]
d = {}
for i in range(2, len(data)):
    line = data[i]
    a = line.split(" = (")
    cle = a[0]
    b = a[1].split(", ")
    v1 = b[0]
    v2 = b[1][:-1]
    d[cle] = [v1, v2]


def suiv(node, letter):
    if letter == 'L':
        return d[node][0]
    else:
        return d[node][1]



def search():
    i = 0
    n = 0
    nodes = [node for node in d if node[-1] == 'A']
    while not all(node[-1] == 'Z' for node in nodes):
        for k in range(len(nodes)):
            nodes[k] = suiv(nodes[k], inst[i])
        i = (i+1) % len(inst)
        n += 1
    print(n)

nodes = [node for node in d if node[-1] == 'A']

def periode(test):
    i = 0
    n = 0
    while test[-1] != 'Z':
        test = suiv(test, inst[i])
        i = (i+1) % len(inst)
        n += 1
    return n

per = [periode(test) for test in nodes]
p = 1
for k in per:
    p = p*k
print(p)

import numpy as np
print(np.lcm.reduce(per))