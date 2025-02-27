
# 873. Length of Longest Fibonacci Subsequence

A sequence `x1, x2, ..., xn` is *Fibonacci-like* if:

- `n >= 3`
- `x_i + x_i+1 == x_i+2` for all `i + 2 <= n`

Given a **strictly increasing** array `arr` of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of `arr`. If one does not exist, return `0`.

A subsequence is derived from another sequence `arr` by deleting any number of elements (including none) from `arr`, without changing the order of the remaining elements. For example, `[3, 5, 8]` is a subsequence of `[3, 4, 5, 6, 7, 8]`.

**Example 1**:

**Input**: arr = [1,2,3,4,5,6,7,8]

**Output**: 5

**Explanation**: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

**Example 2**:

**Input**: arr = [1,3,7,11,12,14,18]

**Output**: 3

**Explanation**: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].

**Constraints**:

- `3 <= arr.length <= 1000`
- `1 <= arr[i] < arr[i + 1] <= 109`

# Solution

Approach 3: Optimized Dynamic Programming
Intuition
We can further optimize our dynamic programming approach by eliminating the hash map lookup. Since our array is strictly increasing, we can take advantage of this ordering to locate valid number pairs more efficiently.

Think about what happens when we're looking for numbers that could precede our current number in a Fibonacci-like sequence. If we have a current number, say 13, we're looking for two previous numbers that sum to 13. This subproblem is actually a very popular problem by itself, known as the Two-Sum problem.

The core idea remains the same: given a number arr[curr], we need to determine whether there exist two numbers arr[start] and arr[end] such that their sum equals arr[curr]. Instead of relying on a hash map to find arr[curr] - arr[end], we can use a two-pointer approach, which is a well-known technique for solving the Two-Sum problem.

Let's understand this with an example. Suppose we have the array [2, 3, 4, 6, 9, 13, 19]. When we're looking at 13 (position 5):

We start with two pointers: start at 2 and end at 9.
If their sum is too large (like 9 + 6 = 15 > 13), we move end left.
If their sum is too small (like 2 + 4 = 6 < 13), we move start right.
When we find a sum that equals 13 (4 + 9 = 13), we've found a valid pair!
This two-pointer approach allows us to get rid of the hash map entirely, saving significant space.

As we iterate through arr, we treat each element as a potential end of a Fibonacci-like sequence. When we find a valid pair (start, end) where arr[start] + arr[end] == arr[curr], we can extend an existing sequence ending at [arr[start], arr[end]] by adding arr[curr]. We track this in a DP table dp[end][curr], setting it to dp[start][end] + 1. This way, we're building longer sequences from shorter ones we've already found.

A subtle but important detail is that we continue searching even after finding a valid pair. This is crucial because there might be multiple pairs that sum to our current number, and we need to consider all of them to find the longest possible sequence.

Similar to the previous approach, we keep track of the maximum value stored in the dp array using a variable maxLen. Remember that dp, and by extension maxLen, stores lengths without counting the first two numbers. So, we need to add 2 to our final answer to include them. If we haven't found any valid sequences (maxLen is 0), we return 0 instead.

Algorithm
Initialize:
a variable n to store the length of the input array.
a 2D array dp of size n × n where dp[prev][curr] stores the length of the Fibonacci sequence ending at indexes prev and curr (excluding the first two numbers).
a variable maxLen to 0 to track the maximum length found (excluding the first two numbers).
For each position curr starting from index 2:
Initialize two pointers:
The start pointer at index 0.
The end pointer at curr - 1.
While the start pointer is less than the end pointer:
Calculate the sum of values at start and end positions.
If the sum is greater than the value at curr:
Decrement the end pointer to try a smaller sum.
If the sum is less than the value at curr:
Increment the start pointer to try a larger sum.
If the sum equals the value at curr:
Update dp[end][curr] by adding 1 to the length of the sequence ending at [start][end].
Update maxLen if the current sequence length is greater.
Move both pointers (increment start and decrement end) to find other possible pairs.
Return maxLen + 2 if maxLen is non-zero (adding 2 to include the first two numbers), otherwise return 0.