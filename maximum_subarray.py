# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

#Final leetcode soln
class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        maxsum = max(nums)
        total = 0
        for i in nums:
            total += i
            if total < 0:
                total = 0
            if i > 0:
                if total > maxsum:
                    maxsum = total
        return(maxsum)

#Initial brute force soln (Failed for array with 1000 elements due to time complexity 1000*1000)
nums = [-2,1,-3,4,-1,2,1,-5,4]
n = len(nums)
maxsum = max(nums)
if n == 1:
    maxsum = nums[0]
for i in range(n):
    total = nums[i]
    for j in range(i + 1, n):
        total = total + nums[j]
        print("Value of i and j", i, j)
        if total > maxsum:
            maxsum = total
print(maxsum)

