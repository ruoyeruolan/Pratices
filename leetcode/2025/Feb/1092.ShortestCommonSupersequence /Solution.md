
# 1092. Shortest Common Supersequence

Given two strings `str1` and `str2`, return the shortest string that has both `str1` and `str2` as **subsequences**. If there are multiple valid strings, return any of them.

A string `s` is a subsequence of string `t` if deleting some number of characters from `t` (possibly `0`) results in the string `s`.

**Example 1**:

**Input**: str1 = "abac", str2 = "cab"

**Output**: "cabac"

**Explanation**:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

**Example 2**:

**Input**: str1 = "aaaaaaaa", str2 = "aaaaaaaa"

**Output**: "aaaaaaaa"

**Constraints**:

- `1 <= str1.length, str2.length <= 1000`
- `str1` and `str2` consist of lowercase English letters.

# Solution

## Overview

We are given two strings, `str1` and `str2`, and our goal is to construct the shortest string that contains both as subsequences. If multiple valid solutions exist, we can return any of them.

A supersequence of a string is a sequence that includes the original string as a subsequence. This means we can derive the original string by removing certain characters without altering the relative order of the remaining ones.

The Shortest Common Supersequence (SCS) is the smallest string that contains both `str1` and `str2` as subsequences.

This problem is closely linked to the Longest Common Subsequence (LCS). A strong understanding of LCS allows us to efficiently construct the SCS. If this concept is unfamiliar, it is highly recommended to first solve the following problems:

# Approach 4: Most Optimal - Space Optimized Dynamic Programming

## Intuition

We can further optimize this problem by defining `dp[row][col]` as the length of the shortest common supersequence (SCS) for the first `row` characters of `str1` and the first `col` characters of `str2` and not the entire sequence like in the previous approach. To build this table, we begin by handling base cases: if one string is empty, the only way to form the supersequence is to take all characters from the other string. This means that `dp[row][0]` = `row` and `dp[0][col]` = `col`, since the SCS of any string with an empty string is just the string itself.

Next, we iterate through both strings and update `dp[row][col]`, based on whether the current characters of `str1` and `str2` match. We have two branches:

1. Matching Characters:
   If `str1[row - 1] == str2[col - 1]`, then this character is part of the SCS, so we extend the solution from `dp[row - 1][col - 1]` by 1: `dp[row][col] = dp[row - 1][col - 1] + 1`

2. Different Characters:
   If `str1[row - 1] != str2[col - 1]`, we must include one of the characters. We choose the option that results in the shorter supersequence: `dp[row][col] = min(dp[row - 1][col]`, `dp[row][col - 1]) + 1`

Here, `dp[row - 1][col]` represents including a character from `str1` and `dp[row][col - 1]` represents including a character from `str2`.

Once the `dp` table is filled, we backtrack from `dp[m][n]` to reconstruct the SCS. The idea is to start at the last cell `(m, n)` and trace back how we reached that value. If characters match, they are added to the result, and both pointers move diagonally. If they differ, we move in the direction that resulted in the smaller value, ensuring that we include necessary characters while keeping the sequence as short as possible. Finally, any remaining characters from `str1` or `str2` are appended to complete the supersequence. Since we build the sequence in reverse, we finally reverse it to obtain the correct order.
