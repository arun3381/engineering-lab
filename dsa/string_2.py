def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sums_optimized(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

print(two_sum([1,2,3,4,5,6,7,8,9,10], 19))
print(two_sums_optimized([1,2,3,4,5,6,7,8,9,10], 19))