def reg_check_nums(nums):
    increasing = False
       
    for i in range(0, len(nums) - 1):
        if i == 0:
            if nums[i + 1] > nums[i]: increasing = True
            else: increasing = False
        else:
            if increasing and nums[i + 1] <= nums[i]: return False
            if not increasing and nums[i + 1] >= nums[i]: return False
        
        if abs(nums[i] - nums[i+1]) >= 1 and abs(nums[i] - nums[i+1]) <= 3: pass
        else: return False    
    return True

def check_nums(anums):
    increasing, nums = False, list()

    for num in anums: nums.append(int(num))
    
    for i in range(len(nums)):
        nums = []
        
        for num in anums: nums.append(int(num))
        nums.pop(i)
        
        if reg_check_nums(nums): return True
        else: continue
    return False
    
with open("day2.in", "r") as file:
    total = 0
    for line in file:
        nums = line.split(" ")
        if check_nums(nums): total += 1
print(total)