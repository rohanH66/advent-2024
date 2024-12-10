with open("day9.in", "r") as file:
    for line in file:
        overall = line
        
print(str(overall))
file_str = ""
file_block = True
index = 0
for i in range(len(overall)):
    try:
        if file_block:
            block = int(overall[i])
            file_str += str(index) * block
            file_str += "." * int(overall[i+1])
            index += 1
        file_block = not file_block
    except: break
overall_list = []
master_copy = []
print(file_str)
for item in file_str:
    overall_list.append(item)
    master_copy.append(item)
    
for i in range(len(master_copy)):
    # print(i - len(overall))
    if i > len(overall_list):
        break
    if master_copy[i] == ".":
        index = -1
        while True:
            if (overall_list[index]).isdigit():
                num = overall_list.pop(index)
                try:
                    overall_list[i] = num
                    break
                except:
                    print(overall_list, i, num)  
            else:
                index -= 1
overall_str = ''
for num in overall_list:
    if num.isdigit():
        overall_str += num     

print(overall_list)
print(overall_str)
total = 0
index = 0
for num in overall_str:
    total += index * int(num)   
    index += 1  
print(total)        