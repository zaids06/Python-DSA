nums=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
min1=nums[0]
for num in nums:
    min1=min(num,min1)
print(min1)