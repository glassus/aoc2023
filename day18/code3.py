data = open('input.txt').read().splitlines()
#data = open('input_test.txt').read().splitlines()

import shapely

# coords = ((0., 0.), (0., 12), (1., 0.))
# polygon = shapely.Polygon(coords)



def parse(line):
    a = line.split(' ')
    return a[0], int(a[1])

def parse2(line):
    a = line.split(' ')
    h = a[2][2:-1]
    val = int(h[:-1], 16)
    dir = int(h[-1])
    direc = {0:'R', 1:'D', 2:'L', 3:'U'}[dir]
    return direc, val


moves = [parse2(line) for line in data]

coords = [(0,0)]
x, y = 0, 0
d = 0
for line in data:
    dir, val = parse2(line)
    if dir == 'U':
        y += val
    if dir == 'D':
        y -= val
    if dir == 'L':
        x -= val
    if dir == 'R':
        x += val
    d += val
    coords.append((x,y))

#coords = [(0,0), (3,0), (3,2), (0,2), (0,0)]
polygon = shapely.Polygon(coords)
aire = polygon.area
print("aire", polygon.area)
print("per", d)
print("final", aire + d//2 + 1)


# import matplotlib.pyplot as plt
# X = [c[0] for c in coords]
# Y = [c[1] for c in coords]
# plt.plot(X,Y,'-')
# plt.show()