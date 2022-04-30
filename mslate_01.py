'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of 
money you can rob tonight without alerting the police.

Sample:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

'''

nums = [2, 3, 5, 12, 13, 16]

## Since we are working with non-adjacent nodes, there can only be two patterns:
## one starting at index 0 and one starting at index 1, with both indices incrementing by 2.
starts = [0, 1]

for start in  starts:  
    i = start
    summary = 0
    while i < len(nums):
        summary = summary + nums[i]
        i = i+2
    print(f"Pattern: {start}: {summary}")



