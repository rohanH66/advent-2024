lst1 = []
lst2, total = [], 0
with open("day1.in", "r") as file:
    for line in file:
        left, right = line.split("   ")
        lst1.append(int(left))
        lst2.append(int(right))

for i in lst1: total += (i * lst2.count(i)) 
    
print(total)