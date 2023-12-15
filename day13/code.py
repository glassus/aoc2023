data = open('input.txt').read().splitlines()
data = open('input_test.txt').read().splitlines()

lst = []
temp = []
for line in data:
    if line == '':
        lst.append(temp)
        temp = []
    else:
        temp.append(line)
lst.append(temp)

def delta(i, taille):
    return min(i, taille - 1 - (i+1))

def test_h_sym(i, tab):
    d = delta(i, len(tab))
    for k in range(0, d+1):
        if tab[i-k] != tab[i+1+k]:
            return False
    return True

def find_h_sym(tab):
    for i in range(len(tab)-1):
        if test_h_sym(i, tab):
            return i
    return None

def same_col(k, p, tab):
    return all(tab[i][k] == tab[i][p] for i in range(len(tab)))

def test_v_sym(j, tab):
    d = delta(j, len(tab[0]))
    for k in range(0, d+1):
        if not same_col(j-k, j+k+1, tab):
            return False
    return True    

def find_v_sym(tab):
    for j in range(len(tab[0])-1):
        if test_v_sym(j, tab):
            return j
    return None


def summerize(tab):
    h = find_h_sym(tab)
    v = find_v_sym(tab)
    
    if h is None:
        h = 0
    else:
        h += 1
        
    if v is None:
        v = 0
    else:
        v += 1

    return 100*h + v

def part1():
    s = 0
    for tab in lst:
        s += summerize(tab)
    print(s)


def find_smuge(tab):
    h = find_h_sym(tab)
    v = find_v_sym(tab)
    if h is None:
        i = 0
        while i < len(tab):
            for k in range(len(tab[0])):
                if tab[i][k] == '#':
                    tab[i][k] = '.'
                else:
                    tab[i][k] = '.'
                th = find_h_sym(tab)
                if th is not None:
                    return i,k
                tv = find_v_sym(tab)
                if tv is not None and tv != v:
                    return i,k                
            