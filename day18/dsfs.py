
line = "R 6 (#70c710)"
a = line.split(' ')
h = a[2][2:-1]
val = int(h[:-1], 16)
dir = int(h[-1])
direc = {0:'R', 1:'D', 2:'L', 3:'U'}[dir]
