import re
overall = []
total = 0
with open("day3.in", "r") as file:
    for line in file:
        index = 0
        print(line)
        
        x = re.findall(r"mul\(([0-9]+),([0-9]+)\)", line)
        
        for tup in x:
            total += int(tup[0]) * int(tup[1])
        overall.append(x)
    print(overall)
    print(total)
