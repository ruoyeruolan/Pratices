
# 2560. House Robber IV

There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array `nums` representing how much money is stashed in each house. More formally, the `i^th` house from the left has `nums[i]` dollars.

You are also given an integer `k`, representing the minimum number of houses the robber will steal from. It is always possible to steal at least `k` houses.

Return the minimum capability of the robber out of all the possible ways to steal at least `k` houses.

**Example 1**:

**Input**: nums = [2,3,5,9], k = 2

**Output**: 5

**Explanation**: 

There are three ways to rob at least 2 houses:

- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.

**Example 2**:

**Input**: nums = [2,7,9,3,1], k = 2

**Output**: 2

**Explanation**: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.

**Constraints**:

- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109
- 1 <= k <= (nums.length + 1)/2

# Solution

## Overview

This is yet another problem based on the House Robber series! This article will assume some prior knowledge of the original version, so you may want to solve that before this one. So before diving in, let's quickly recall the core idea behind the original problem.

In the classic House Robber problem, the goal is to maximize the total amount stolen from a row of houses while following one key restriction: the robber cannot rob two consecutive houses. This forces the robber into a branched decision making process that at each house, they must choose whether to rob it or skip it. If they robs it, they must add its value to the best amount stolen from two houses before. If they skips it, they simply takes the best amount stolen from the previous house. This naturally leads to a recursive relationship:

maxAmount(houseNumber) = max(maxAmount(houseNumber - 1), maxAmount(houseNumber - 2) + amount(houseNumber))

Using dynamic programming, we can store these values and efficiently compute the maximum amount the robber can steal.

In this current problem, the robber still has to follow the restraint that they cannot steal from two consecutive houses. However, this time, instead of maximizing the total reward, they want to maximize the minimum amount stolen amongst all houses.

Similar to the original problem, we can think of a recursive relation to solve this. Again, we have two choices:

Rob the current house (but then we must skip the next house).
Skip the current house and move forward.
However, unlike the original problem, we need an additional condition—ensuring that we rob at least k houses. The dynamic programming solution involves a state dp[houseIndex][numberOfHousesRobbed]. Since we iterate over n houses and track up to k robbed houses, the problem becomes more complex, and solving it with dynamic programming takes O(n⋅k) time.

Problems that require maximizing the minimum or minimizing the maximum often suggest a binary search approach. Instead of searching through indices or subsets directly, we can binary search on the reward value itself. By determining whether a given minimum reward is achievable, we can efficiently narrow down the possible solutions. If you're unfamiliar with this technique, you can refer to this guide to learn more about binary search.

Approach: Binary Search
Intuition
Instead of focusing on maximizing a total sum, we need to guarantee that the minimum amount stolen from any robbed house is as large as possible. A brute force approach would involve checking every possible way to rob k houses while obeying the adjacency constraint, but this would be too slow for large inputs.

A more efficient way to approach this problem is to recognize that we are trying to push the minimum stolen amount as high as possible while still satisfying the condition of robbing at least k houses. This naturally leads to using binary search on the minimum reward that the robber can secure.

We define the search space based on the possible values for this minimum reward. The smallest possible amount we can steal from any house is 1 (assuming all house values are at least 1), and the largest possible value is the maximum house reward in the array. This gives us a range of [1, maxReward], where maxReward is the highest value in the list of houses.

We use binary search to determine the maximum possible minimum reward. At each step, we take the middle value in our range (midReward = (minReward + maxReward) / 2) and check whether it's possible to rob at least k houses while ensuring that each stolen amount is at least midReward.

To determine whether a particular midReward is feasible, we use a greedy approach. We iterate through the list of house values and select houses that offer at least midReward. Since we cannot rob consecutive houses, we skip the next house each time we choose one. We keep a count of how many houses have been robbed, and if we reach at least k houses, it means the current midReward is achievable.

If it is possible to rob at least k houses with the current midReward, then we try increasing it by moving the binary search range to the right (minReward = midReward + 1).
If it is not possible, it means midReward is too high, so we reduce it by moving the search range to the left (maxReward = midReward - 1).
By continuously adjusting our search range, we eventually find the highest possible value of midReward that still allows robbing at least k houses.