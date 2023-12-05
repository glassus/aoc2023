data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()
import portion as P

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

for i in range(len(maps)):
    maps[i] = sorted(maps[i], key= lambda x:x[1])



def passage_map(val, mapp):
    if val < mapp[0][1]:
        return val
    if val >= mapp[-1][1] + mapp[-1][2]:
        return val
    for lst in mapp:
        d, s, r = lst
        if s <= val < s + r:
            trans_val = d + val - s
            return trans_val
    #return trans_val

tp = {}

def total_passage(val):
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
        nval = total_passage(val)
        mini = min(nval, mini)
    return mini

#def part2():
mini = 10**100
i = 0
while i < len(seeds)-1:
    print(i)
    for val in range(seeds[i], seeds[i]+seeds[i+1]):
        #print(val)
        nval = total_passage(val)
        mini = min(nval, mini)
        #print(val, nval)
    i += 2
print(mini)


def create_union():
    d, s, r = maps[0][0]
    a = P.closed(s, s+r-1)
    for mapp in maps:
        for lst in mapp:
            d, s, r = lst
            a = a | P.closed(s, s+r-1)
    return a