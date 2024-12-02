def check_nums(anums):
    increasing, nums = False, list()
    
    for num in anums: nums.append(int(num))
    
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
    
with open("day2.in", "r") as file:
    total = 0
    for line in file:
        nums = line.split(" ")
        if check_nums(nums): total += 1
print(total)