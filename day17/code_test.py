data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

m = {}
mem = {}
d = {}
for i in range(len(data)):
    for k in range(len(data[0])):
        pos = k - i*1j
        d[pos] = int(data[i][k])

H = len(data)
W = len(data[0])

def dir_voisins(pos, cpt, old_dir):
    lst = []
    dir = [-1, 1, 1j, -1j]
    for dep in dir:
        npos = pos + dep
        if (0 <= npos.real < W)  and  (0 <= -npos.imag < H):
            if (cpt < 3 or dep != old_dir) and dep != -1*old_dir: 
                lst.append(dep)
    return lst

start = (0, 0, 0)
end = W-1-(H-1)*1j
m[start[0]] = 0
file = [start]
parent = {}

while file:
    file = sorted(file, key = lambda x : m[x[0]])
    curr, cpt, old_dir = file.pop(0)
    dir_vois = dir_voisins(curr, cpt, old_dir)
    
    for dir in dir_vois :

        newpos = curr + dir

        if newpos not in m:
            m[newpos] = m[curr] + d[newpos]
            parent[newpos] = curr
            if dir != old_dir:
                file.append((newpos, 1, dir))
                mem[newpos] = (1, dir)
            else:
                file.append((newpos, cpt+1, dir))
                mem[newpos] = (cpt+1, dir)
        else:
            if m[curr] + d[newpos]  <= m[newpos]:
                m[newpos] = m[curr] + d[newpos]
                parent[newpos] = curr
                if dir != old_dir:
                    file.append((newpos, 1, dir))
                    mem[newpos] = (1, dir)
                else:
                    file.append((newpos, cpt+1, dir))
                    mem[newpos] = (cpt+1, dir)
            


def remonte():
    curr = W-1-(H-1)*1j
    while curr != 0:
        d[curr] = 0
        curr = parent[curr]

def affiche():
    for i in range(len(data)):
        s = ''
        for k in range(len(data[0])):
            pos = k - i*1j  
            s += str(d[pos])
        print(s)

remonte()
affiche()
print(m[W-1-(H-1)*1j])