data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

def voisins(pos):
    lst = []
    d = [-1, 1, 1j, -1j]
    for dep in d:
        npos = pos + dep
        if (0 <= npos.real < len(data[0])) \
           and  (0 <= -npos.imag < len(data)):
            lst.append(npos)
    return lst

def dict_from_data(data):
    d = {}
    for i in range(len(data)):
        for k in range(len(data[0])):
            pos = k - i*1j
            if data[i][k] == '#':
                d[pos] = data[i][k]
    return d
            
def expand(data):
    lines_to_double = []
    for i in range(len(data)):
        if data[i] == '.'* len(data[0]):
            lines_to_double.append(i)
    lines_to_double.reverse()
    for i in lines_to_double:
        data.insert(i, '.'* len(data[0]))
    
    rows_to_double = []
    for j in range(len(data[0])):
        if all(data[i][j] == '.' for i in range(len(data))):
            rows_to_double.append(j)
    rows_to_double.reverse()
    for j in rows_to_double:
        for i in range(len(data)):
            data[i] = data[i][:j] + '.' + data[i][j:]
    return data

#data = expand(data)
d = dict_from_data(data)

def BFS_from(pos):
    #inutile..........
    dist = {pos:0}
    file = [pos]
    while file:
        curr = file.pop(0)
        for p in voisins(curr):
            if (p not in dist) or (p in dist and dist[p] > dist[curr] + 1):
                dist[p] = dist[curr] + 1
                file.append(p)
    return dist

def dist(posA, posB):
    diff = posB - posA
    return int(abs(diff.real) + abs(diff.imag))

def part1():
    galaxies = list(d.keys())
    s = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            s += dist(galaxies[i], galaxies[j])
    return s

def lines_and_rows_to_expand(data):
    lines_to_double = []
    for i in range(len(data)):
        if data[i] == '.'* len(data[0]):
            lines_to_double.append(i)
    lines_to_double.reverse()
    
    rows_to_double = []
    for j in range(len(data[0])):
        if all(data[i][j] == '.' for i in range(len(data))):
            rows_to_double.append(j)
    rows_to_double.reverse()

    return lines_to_double, rows_to_double

def expand_n(data, n):
    galaxies = list(d.keys())
    next_pos = {pos:pos for pos in galaxies}
    lines_to_double, rows_to_double = lines_and_rows_to_expand(data)
    for k in rows_to_double:
        for pos in galaxies:
            if pos.real > k:
                next_pos[pos] += n
    for i in lines_to_double:
        for pos in galaxies:
            if pos.imag < -i:
                next_pos[pos] -= n*1j
    return list(next_pos.values())
    
    

def part2(n):
    lst = expand_n(data,n-1)
    s = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            s += dist(lst[i], lst[j])
    return s    