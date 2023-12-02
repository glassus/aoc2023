data = open('input.txt').read().splitlines()
#data = open('input_test2.txt').read().splitlines()

def is_number(c):
    return 48 <= ord(c) <= 57

def numbers(line):
    return [c for c in line if is_number(c)]

def extremes(line):
    lst = numbers(line)
    return int(lst[0]+lst[-1])

def part1():
    return sum(extremes(line) for line in data)

num_text = ["one", "two", "three", "four", "five", "six", \
            "seven", "eight", "nine"]

first_occ_text = {txt:None for txt in num_text}

def search_first_word(line):
    mini = 10**9
    num = None
    for word in num_text:
        idx = line.find(word)
        if idx == -1:
            idx = 10**9
        if idx < mini:
            mini = idx
            num = word
    return num, mini

def search_first_num(line):
    for i in range(len(line)):
        if is_number(line[i]):
            return line[i], i
    return None, 10**9

def first_of_all(line):
    txt, itxt = search_first_word(line)
    num, inum = search_first_num(line)
    if itxt < inum:
        return txt
    else:
        return num

num_text_reversed = [txt[::-1] for txt in num_text]

def search_last_word(line):
    line = line[::-1]
    mini = 10**9
    num = None
    for word in num_text_reversed:
        idx = line.find(word)
        if idx == -1:
            idx = 10**9
        if idx < mini:
            mini = idx
            num = word
    if num is not None:
        num = num[::-1]
    return num, mini

def search_last_num(line):
    line = line[::-1]
    for i in range(len(line)):
        if is_number(line[i]):
            return line[i], i
    return None, 10**9

def last_of_all(line):
    txt, itxt = search_last_word(line)
    num, inum = search_last_num(line)
    if itxt < inum:
        return txt
    else:
        return num
    
def word_to_txt(w):
    return str(num_text.index(w)+1)

def num_total(line):
    f = first_of_all(line)
    l = last_of_all(line)
    if f in num_text:
        f = word_to_txt(f)
    if l in num_text:
        l = word_to_txt(l)
    return int(f+l)

def part2():
    return sum(num_total(line) for line in data)