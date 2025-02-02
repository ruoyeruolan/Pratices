<!-- @leetcode -->

# 1752. Check if Array Is Sorted and Rotated

Given an array `nums`, return `true` if the array was originally sorted in **non-decreasing** order, then rotated some number of positions (including zero). Otherwise, return `false`.

There may be **duplicates** in the original array.

Note: An array A rotated by `x` positions results in an array `B` of the same length such that `A[i] == B[(i+x) % A.length]`, where `%` is the modulo operation.

**Example 1**:

**Input**: nums = [3,4,5,1,2]

**Output**: true

**Explanation**: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

**Example 2**:

**Input**: nums = [2,1,3,4]
**Output**: false
**Explanation**: There is no sorted array once rotated that can make nums.

**Example 3**:

**Input**: nums = [1,2,3]

**Output**: true

**Explanation**: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.

**Constraints**:

- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

# Solution

## Overview

We need to find whether the given integer array `nums` could represent a sorted array that has been rotated some number of times. A sorted array is defined as one arranged in non-decreasing order, meaning each element is less than or equal to the next. A rotation involves shifting a contiguous block of elements to the back of the array, preserving the relative order of all elements.

For example, `[3, 4, 5, 1, 2]` is a rotated version of the sorted array `[1, 2, 3, 4, 5]`. On the other hand, `[3, 4, 2, 1, 5]` is not a valid rotation of any sorted array because the order of elements is not preserved.

## Approach3: Find Smallest Element

## Intuition

To find whether an array can be sorted by rotation, we need to check if, after a certain point, the sequence of elements remains sorted in a cyclic manner. A more efficient way to do this is by finding the smallest element in the array and using its position to identify the potential rotation offset, which would be the point where the original sorted array begins.

Once we identify the smallest element, we treat it as the "starting" point of the sorted array. From this position, we check if the next `n` elements, wrapping around cyclically, form a sorted sequence.

The key observation here is that, in a sorted array that has been rotated, **all elements should be in non-decreasing order**, except for one place where the largest element will be followed by the smallest element due to the rotation. This results in at most one "inversion" — a pair where a number is greater than the next one.

If there are more than one such "inversions," meaning multiple instances where a number is greater than its successor, the array cannot be sorted through any rotation. If there’s at most one inversion, then the array can indeed be sorted by a rotation.

Let's consider an example with the array `nums = [3, 4, 5, 1, 2]`. The smallest element is `1`, which we treat as the start of the sorted array. Starting from 1, the sequence `[1, 2, 3, 4, 5]` is sorted in a cyclic manner, with only one inversion: `5` is followed by `1`, which is expected in a rotated sorted array. Since there is only one inversion, the array can be sorted by rotation, and we return true.

## Algorithm

- Check if the array is empty or contains only one element. If so, return `true`, as a single element or an empty array is trivially sorted.

- Count the number of inversions (pairs where `nums[i] > nums[i + 1]`) in the array:

- Iterate through the array from `1` to `n - 1`.

- For each element, compare it with the previous element. If the current element is smaller, increment the inversion count.

- Compare `nums[n - 1]` with `nums[0]`. If `nums[0] < nums[n - 1]`, increment the inversion count.

- If the total inversion count is less than or equal to 1, return true. Otherwise, return false.
