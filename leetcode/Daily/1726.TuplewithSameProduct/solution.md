<!-- @leetcode -->

# 1726. Tuple with Same Product

Given an array `nums` of **distinct** positive integers, return the number of tuples (a, b, c, d) such that `a * b = c * d` where `a`, `b`, `c`, and `d` are elements of nums, and `a != b != c != d`.

**Example 1**:

**Input**: nums = [2,3,4,6]
**Output**: 8
**Explanation**: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

**Example 2**:

**Input**: nums = [1,2,4,5,10]
**Output**: 16
**Explanation**: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

**Constraints**:

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 104`
- All elements in nums are distinct.

# Solution

## Overview

We are given an array `nums` containing `n` distinct positive integers. The goal is to find the number of tuples `(a, b, c, d)` such that:

- `a`, `b`, `c`, and `d` are distinct elements of the `nums` array, and
- The condition `a * b == c * d` is satisfied.

Note, that a tuple refers to an ordered list of 4 elements. This means the tuples `(2, 3, 1, 6)` and `(3, 2, 1, 6)` are considered distinct and counted separately.

In fact, if we have two pairs of numbers `{a, b}` and `{c, d}` that satisfy `a * b == c * d`, we can generate multiple distinct tuples by varying the order of the elements and the pairs:

- `(a, b, c, d)`
- `(b, a, c, d)`
- `(a, b, d, c)`
- `(b, a, d, c)`
- `(c, d, a, b)`
- `(c, d, b, a)`
- `(d, c, a, b)`
- `(d, c, b, a)`

To understand this, observe that for every two pairs of distinct numbers `{a, b}` and `{c, d}`, there are three independent ways to reorder the elements and pairs:

1. Within each pair:

- The order of elements in `{a, b}` can be `(a, b)` or `(b, a)` (2 options).
- Similarly, the order in `{c, d}` can be `(c, d)` or `(d, c)` (2 options).

2. Between the pairs:

- The order of the two pairs can be `({a, b}, {c, d}) or ({c, d}, {a, b})` (2 options).

Since these choices are independent, the total number of distinct tuples is the product of these options: `2×2×2=8`.

## Approach 3: Product Frequency Hash Map

### Intuition

In the previous approach, we identified a bottleneck caused by sorting the pairProducts array to calculate the frequency of each element. To address this, instead of storing each pair product in a new array, we will directly update the frequency of each product using a hash map. Then, following the same approach as before, we will count the number of pairs of products with the same value and calculate how many tuples can be formed from them.

> **Note: For a more comprehensive understanding of hash tables, check out the Hash Table Explore Card 🔗. This resource provides an in-depth look at hash tables, explaining their key concepts and applications with a variety of problems to solidify understanding of the pattern.

### Algorithm

- Initialize
  - `numsLength` to the length of the `nums` array.
  - a hash map, `pairProductsFrequency`.
  - `totalNumberOfTuples` to `0`.

- Iterate over ``nums`` with `firstIndex` from `0` to `numsLength - 1`:
  - Iterate over `nums` with `secondindex` from `firstIndex + 1` to `numsLength - 1`:
    - Increment the frequency of the product: `nums[firstIndex] * nums[secondindex]` by `1`.

- For each element `[productValue, productFrequency]` of `pairProductsFrequency`:
  - Calculate the number of pairs of products with value `productValue`: `pairsOfEqualProduct = (productFrequency - 1) * productFrequency / 2`.
  - Add all possible tuples for that product value to the total: increment `totalNumberOfTuples` by `8 * pairsOfEqualProduct`.

- Return `totalNumberOfTuples`.
