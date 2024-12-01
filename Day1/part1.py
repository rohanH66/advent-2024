lst1, lst2, total = [], [], 0
with open("day1.in", "r") as file:
    for line in file:
        left, right = line.split("   ")
        lst1.append(int(left))
        lst2.append(int(right))

lst1, lst2 = sorted(lst1), sorted(lst2)

for i in range(len(lst1)): total += abs(lst1[i] - lst2[i]) 
    
print(total)