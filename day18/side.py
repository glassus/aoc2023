line = '##..##.......'
def compte(line):
    i = 0
    n = 0
    inside = False
    while i < len(line):
        v = 0
        while i < len(line) and line[i] == '.':
            i += 1
            if inside:
                v += 1
        if i < len(line):        
            n += v
        inside = not inside
        while i < len(line) and line[i] == '#':
            i += 1
            n += 1
    return n

print(compte(line))