import re
total, check = 0, True
with open("day3.in", "r") as file:
    for line in file:        
        x = re.findall(r"(don't\(\)|do\(\)|mul\([0-9]+,[0-9]+\))", line)
        for item in x:
            if item == "do()": check = True
            elif item == "don't()": check = False
            elif check:
                temp = item[4:].split(",")
                total += int(temp[0]) * int(temp[1].replace(")", ""))
print(total)