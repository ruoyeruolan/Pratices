
# 1780. Check if Number is a Sum of Powers of Three

Given an integer `n`, return `true` if it is possible to represent `n` as the sum of **distinct powers of three**. Otherwise, return `false`.

An integer `y` is a power of three if there exists an integer `x` such that `y == 3x`.

**Example 1**:

**Input**: n = 12

**Output**: true

**Explanation**: 12 = 31 + 32

**Example 2**:

**Input**: n = 91

**Output**: true

**Explanation**: 91 = 30 + 32 + 34

**Example 3**:

**Input**: n = 21

**Output**: false

**Constraints**:

- `1 <= n <= 107`

# Solution

## Approach 3: Ternary Representation

### Intuition

First, let's break the problem down into a more familiar one. We know that every number can be written as a sum of distinct powers of 2 — in other words, every number has a unique binary representation. A simple way to find the binary representation of a number is by repeatedly taking its remainder when divided by 2 (mod 2) and then dividing the number by 2 to move to the next bit. This method is similar to the two’s complement approach.

In this problem, we apply the same logic but in base 3 instead of base 2. We construct the ternary representation of the given number by taking its remainder when divided by 3 (mod 3) and then dividing it by 3 to proceed to the next digit. If any of these remainders equals 2, we would need to use a power of 3 twice, which is not allowed. In that case, we immediately return false.