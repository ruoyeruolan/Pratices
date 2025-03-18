
# 3356. Zero Array Transformation II

You are given an integer array `nums` of length `n` and a 2D array queries where `queries[i] = [l_i, r_i, val_i]`.

Each `queries[i]` represents the following action on nums:

- Decrement the value at each index in the range `[l_i, r_i]` in `nums` by at most `val_i`.
- The amount by which each value is decremented can be chosen independently for each index.
- A Zero Array is an array with all its elements equal to `0`.

Return the minimum possible non-negative value of `k`, such that after processing the first `k` queries in sequence, `nums` becomes a Zero Array. If no such k exists, return`-1`.

**Example 1**:

**Input**: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

**Output**: 2

**Explanation**:

For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

**Example 2**:

**Input**: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

**Output**: -1

**Explanation**:

For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.

**Constraints**:

- `1 <= nums.length <= 105`
- `0 <= nums[i] <= 5 * 105`
- `1 <= queries.length <= 105`
- `queries[i].length == 3`
- `0 <= li <= ri < nums.length`
- `1 <= vali <= 5`

# Solution

## Overview

We are given an integer array `nums` of length `n`, and a list of queries that are each in the form `[left, right, val]`. For a given range `[left, right]`, we can decrease each element in that range by at most `val`. Our task is to determine the earliest query that allows us to turn nums into an array of all zeroes. If it's not possible, we return `-1`.

From this example, we can see that there are two main operations that will occur:

1. Iterating through each element in queries.
2. Applying the range and value of each query to `nums`.

We need to assess how to optimally handle both operations to find the earliest value of `k` to reach a zero array.

## Approach 1: Binary Search

### Intuition

A simple approach would be to iterate through each query, applying the updates directly to `nums` and checking whether all elements have become zero. However, given the constraints where both nums and queries can be as large as 10^5, this approach is too slow. Each query might require traversing the entire array, leading to an impractical time complexity.

To optimize this, we need a more efficient way to apply queries to `nums`. Instead of modifying each element individually, we can take advantage of a difference array. This technique allows us to apply a range update in constant time. The key idea is to store the changes at the boundaries of the range rather than updating every element inside it. For a query `[left,right,val]`, we add `val` at index `left`, and subtract `val` at index `right + 1`. When we later compute the prefix sum of this difference array, it reconstructs the actual values efficiently. This way, instead of updating nums repeatedly, we can process all queries in an optimized manner and then traverse `nums` just once to check if all elements have become zero.

Now that we optimized how we apply queries, the next step is to determine how many queries we actually need. Instead of processing all queries one by one, we can use binary search to quickly determine the minimum number of queries required to achieve the zero array. We start by setting two pointers: `left = 0` and `right = len(queries)`, representing the search range. The middle index, `mid = (left + right) // 2`, represents the number of queries we will attempt to apply. We update `nums` using only the first mid queries, compute the final state using the prefix sum of the difference array, and check if `nums` is now a zero array.

If it is possible to achieve a zero array with mid queries, we reduce our search range by setting `right = mid - 1`, since we might be able to do it with even fewer queries. Otherwise, we increase our search range by setting `left = mid + 1`, since we need more queries to reach the desired state. This binary search ensures that instead of checking every possible number of queries linearly `O(N)`, we find the answer in `O(logN)` time.

```python
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        left, right = 0, len(queries)

        # Zero array isn't formed after all queries are processed
        if not self.can_form_zero_array(nums, queries, right):
            return -1

        # Binary Search
        while left <= right:
            middle = left + (right - left) // 2
            if self.can_form_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1

        # Return earliest query that zero array can be formed
        return left

    def can_form_zero_array(
        self, nums: List[int], queries: List[List[int]], k: int
    ) -> bool:
        n = len(nums)
        total_sum = 0
        difference_array = [0] * (n + 1)

        # Process query
        for query_index in range(k):
            start, end, val = queries[query_index]

            # Process start and end of range
            difference_array[start] += val
            difference_array[end + 1] -= val

        # Check if zero array can be formed
        for num_index in range(n):
            total_sum += difference_array[num_index]
            if total_sum < nums[num_index]:
                return False
        return True
```

## Approach 2: Line Sweep

### Intuition_

In our previous approach, we used binary search to determine how many queries were needed to turn nums into a zero array. This allowed us to efficiently process a subset of queries, applying them to a difference array, and then checking if nums had become all zeros. While this was an improvement over a naive approach, there was still an inefficiency: we were iterating over queries twice: once for binary search and again while applying updates.

To optimize further, we can change our perspective on how we traverse the data. Instead of iterating through queries, we can iterate directly through nums, using it as the main loop. This means that as we process each element in nums, we dynamically apply only the necessary queries at the right moment. The key challenge, then, is finding an efficient way to apply queries while moving through nums.

This is where a line sweep approach comes into play. Line sweeping is a technique that processes an array incrementally, maintaining only the relevant updates at each step. Instead of processing all queries upfront, we maintain an active set of queries and update nums only when necessary. Here, the difference array helps us track how nums is being modified, while queries provide the updates at specific points.

We start at index 0 of nums and check if it can be turned into 0 with the queries we have processed so far. If it cannot be zeroed out, we process additional queries to apply their effects. The key observation is that at any index i in nums, a query [left, right, val] can fall into three possible cases:

If i < left, the query affects a later part of nums, so we store it for later processing.
If left ≤ i ≤ right, the query is immediately relevant and should be applied.
If right < i, the query is no longer useful for the current index and can be ignored.
For example, if we're at index 4 in nums and the current query accesses the range [0,2], we do not need to process that query and can simply move on to the next query.

Otherwise, we continue to the next element of nums. We repeat this process until we reach the end of either nums or queries, where we then return either k or -1, respectively.

Through this process, we only have to iterate through both nums and queries at most once each while skipping over unnecessary queries.

```python
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        total_sum = 0
        k = 0
        difference_array = [0] * (n + 1)

        # Iterate through nums
        for index in range(n):
            # Iterate through queries while current index of nums cannot equal zero
            while total_sum + difference_array[index] < nums[index]:
                k += 1

                # Zero array isn't formed after all queries are processed
                if k > len(queries):
                    return -1

                left, right, val = queries[k - 1]

                # Process start and end of range
                if right >= index:
                    difference_array[max(left, index)] += val
                    difference_array[right + 1] -= val

            # Update prefix sum at current index
            total_sum += difference_array[index]

        return k
```
