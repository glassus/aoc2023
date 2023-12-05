data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
import portion as P
from copy import deepcopy

seeds = [int(k) for k in data[0].split(': ')[1].split()]

maps = [[] for _ in range(7)]
k = -1
for i in range(1, len(data)):
    line = data[i]
    if 'map' in line:
        k += 1
        continue
    if line == '':
        continue
    rule = [int(k) for k in line.split()]
    maps[k].append(rule)


invmaps = deepcopy(maps[::-1])
for map in invmaps:
    for lst in map:
        lst[0], lst[1] = lst[1], lst[0]
    



for i in range(len(maps)):
    maps[i] = sorted(maps[i], key= lambda x:x[1])



def passage_map(val, mapp):
    trans_val = val
    for lst in mapp:
        d, s, r = lst
        if s <= val < s + r:
            trans_val = d + val - s
            return trans_val
    return trans_val

tp = {}

def total_passage(val, maps):
    if val in tp:
        return tp[val]
    oval = val
    for mapp in maps:
        val = passage_map(val, mapp)
    tp[oval] = val
    return val

def part1():
    mini = 10**9
    for val in seeds:
        nval = total_passage(val, maps)
        mini = min(nval, mini)
    return mini



mini_seed = 10**10
for i in range(0, len(seeds), 2):
    mini_seed  = min(mini_seed , seeds[i])



def union_seeds():
    i = 2
    a = P.closed(seeds[0], seeds[0]+seeds[1])
    while i < len(seeds)-1:
        a = a | P.closed(seeds[i], seeds[i]+seeds[i+1])
        i += 2
    return a

union = union_seeds()

def part2(maps):
    i = 0
    while total_passage(i, maps) not in union:
        if i % 100000 == 0:
            print(i)
        i += 1
    return i

sol_part2 = part2(invmaps)