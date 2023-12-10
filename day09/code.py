data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

seq = []
for line in data:
    seq.append([int(k) for k in line.split()])


lst = [10,  13,  16,  21,  30,  45]

def extra(lst):
    last = []
    while not all(k == 0 for k in lst):
        last.append(lst[0])
        for i in range(len(lst)-1):
            lst[i] = lst[i+1] - lst[i]
        lst.pop()
        
        
    s = 0
    for v in range(len(last)-1,-1,-1):
        s = last[v] - s
    return s

print(sum(extra(lst) for lst in seq))

