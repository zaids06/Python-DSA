nums = [9,23,1,4,55,33]
for i in range (0,len(nums)-1):
    min=i
    for j in range (i+1,len(nums)):
        if nums[j]<nums[min]:
            min=j
    nums[i],nums[min]=nums[min],nums[i]
print (nums)