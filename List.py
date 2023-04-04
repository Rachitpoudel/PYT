nums = [1,2,3,4,5,6,7,8,9]
nums.append(6)
nums.insert(3,"A")
nums.remove(5)
nums.extend(["a","b","c"])
len(nums)
del nums[4]
for i in nums:
    print(i)
nums_copy = nums
nums.append("z")
print(nums_copy)
print(nums, len, type(nums))