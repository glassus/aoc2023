data = open('input.txt').read().splitlines()
#data = open('input_test2.txt').read().splitlines()

def numbers(line):
    return [c for c in line if c.isdigit()]

def extremes(line):
    lst = numbers(line)
    return int(lst[0]+lst[-1])

def part1():
    return sum(extremes(line) for line in data)

num_text = ["one", "two", "three", "four", "five", "six", \
            "seven", "eight", "nine"]

conv = {txt:txt[0]+str(num_text.index(txt)+1)+txt[-1] for txt in num_text}

def transf(line):
    line_mod = ""
    while line_mod != line:
        line_mod = line
        for w in num_text:
            line = line.replace(w, conv[w])
    return line


def part2():
    return sum(extremes(transf(line)) for line in data)