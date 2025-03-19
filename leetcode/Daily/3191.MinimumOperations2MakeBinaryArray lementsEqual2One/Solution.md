
# 3191. Minimum Operations to Make Binary Array Elements Equal to One I

You are given a **binary array** `nums`.

You can do the following operation on the array any number of times (possibly zero):

- Choose any `3` consecutive elements from the array and flip all of them.

**Flipping** an element means changing its value from `0` to `1`, and from `1` to `0`.

Return the **minimum number of operations** required to make all elements in `nums` equal to `1`. If it is impossible, return `-1`.

**Example 1**:

**Input**: nums = [0,1,1,1,0,0]

**Output**: 3

**Explanation**:

We can do the following operations:

Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].

**Example 2**:

**Input**: nums = [0,1,1,1]

**Output**: -1

**Explanation**:

It is impossible to make all elements equal to 1.

**Constraints**:

- `3 <= nums.length <= 10^5`
- `0 <= nums[i] <= 1`

# Solution

## Overview

We are given a binary array `nums`, and we need to transform all elements into `1` using a specific operation. The allowed operation lets us choose any **three consecutive elements** and flip all of them (changing `0` to `1` and `1` to `0`). Our task is to determine the minimum number of operations required to turn the entire array into all `1s`. If it is impossible to achieve this transformation, we return `-1`.

Since we can only flip three consecutive elements at a time, isolated `0s` or certain patterns of `0s` may prevent us from turning everything into `1`. If the number of `0s` in certain positions makes it impossible to fully eliminate them using groups of three, the transformation cannot be achieved.

Before discussing the approaches, let's review a fundamental property of XOR:

**Parity Invariance**:

Parity invariance means that the number of times a position is flipped determines its final value. If a position is flipped an odd number of times, its value changes, but if it is flipped an even number of times, it stays the same.

Consider the array `[1, 0, 0, 1, 0, 1, 1]`. We start by flipping three consecutive elements to try and transform all `0s` into `1s`. First, flipping the subarray `[0, 0, 1]` at indices `1...3` changes the array to `[1, 1, 1, 0, 0, 1, 1]`. Then, flipping `[0, 0, 1]` at indices `3...5` gives `[1, 1, 1, 1, 1, 0, 1]`. Finally, flipping `[1, 0, 1]` at indices `4...6` results in [`1, 1, 1, 1, 0, 1, 0]`.

At this point, we see that the `0s` at positions `4` and `6` remain, and there is no way to flip them without also flipping other elements. Since we can only flip three elements at a time, we cannot isolate these `0s` in a way that allows us to change them to `1s`. This happens because these positions were flipped an even number of times, so they retained their original value. Because of this parity constraint, the transformation is impossible, and we must return `-1`.

## Approach 1: Using Deque

### Intuition

**The first observation is that if a `0` appears near the end of the array (specifically within the last two positions), we cannot flip it using a full triplet. This means that if any `0` is left in the last two places after processing, it is impossible to make the entire array `1`, so we return `-1`**.

Since a single flip operation affects three elements, each flip we apply has a lasting effect on the next two indices. Instead of modifying the entire array and recomputing values every time, we need a way to keep track of the flips already applied. This is where we introduce a deque to store the indices of past flips. The deque allows us to efficiently determine how many times each index has been flipped by keeping only the flips that are still affecting the current index.

We iterate through the array from left to right. At each index `i`, we first remove any outdated flips from the deque and those that were applied more than two positions earlier, as they no longer affect `i`.

Next, we determine whether we need to flip at index `i`. The second key observation is that the effect of a flip is cumulative: if an index has been flipped an odd number of times, it has effectively changed its value, whereas if it has been flipped an even number of times, it remains the same as its original value. Using this property, we can check:

`(original value of nums[i])+(number of active flips affecting i)mod2`

If the result is `0`, it means that `nums[i]` is currently `0`, so we must flip it.
To flip, we check if `i + 2` is within bounds (since we need a full triplet). If not, we return `-1`. Otherwise, we record this flip by adding i to the deque and incrementing the operation count.

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flip_queue = deque()  # Stores indices of flip operations
        count = 0  # Number of operations performed

        for i in range(len(nums)):
            # Remove expired flips (older than 3 indices)
            while flip_queue and i > flip_queue[0] + 2:
                flip_queue.popleft()

            # If the current element needs flipping
            if (nums[i] + len(flip_queue)) % 2 == 0:
                # Cannot flip a full triplet
                if i + 2 >= len(nums):
                    return -1
                count += 1
                flip_queue.append(i)

        return count
```

## Approach 2: Sliding Window

### Intuition_

In the previous approach, we used a deque to track active flips and determine how many times each index had been flipped. Now, we take a different approach by modifying the array directly as we iterate. The core idea remains the same: flipping three consecutive elements at a time while ensuring that every 0 gets converted to 1 in the most efficient way possible.

Instead of maintaining a separate structure to track flips, we will scan the array from left to right and only focus on the last element of each triplet to determine if a flip is needed. This means that for each index i, we check whether nums[i - 2] is still 0. If it is, then we must flip the triplet ending at i (nums[i - 2], nums[i - 1], nums[i]).

By flipping in this way, we ensure that every 0 gets handled at the earliest possible opportunity, preventing any unflippable 0s from being left behind. This also ensures that we are using the minimum number of operations because each flip is only applied when absolutely necessary.

We iterate through the array, ensuring that at every position i, we can check the last element of a full triplet (nums[i - 2]). If nums[i - 2] is 0, we immediately flip nums[i - 2], nums[i - 1], and nums[i], and we increase the flip count.

After processing all indices, we check if the entire array has been turned into 1s. If the sum equals the length of the array, it means every element is 1, so we return the total number of flips. Otherwise, we return -1, indicating that it was impossible to transform the entire array.

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(2, len(nums)):

            # only looking forward to the last element
            if nums[i - 2] == 0:
                count += 1
                # flip i-2 and i-1 and i
                nums[i - 2] = nums[i - 2] ^ 1
                nums[i - 1] = nums[i - 1] ^ 1
                nums[i] = nums[i] ^ 1

        if sum(nums) == len(nums):
            return count
        return -1
```
