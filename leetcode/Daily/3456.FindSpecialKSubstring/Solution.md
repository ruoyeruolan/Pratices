
# 3456. Find Special K Substrings

You are given a string `s` and an integer `k`.

Determine if there exists a substring of length exactly `k` in s that satisfies the following conditions:

- The substring consists of only **one distinct character** (e.g., "aaa" or "bbb").
- If there is a character immediately before the substring, it must be different from the character in the substring.
- If there is a character immediately after the substring, it must also be different from the character in the substring.

Return `true` if such a substring exists. Otherwise, return `false`.

**Example 1**:

**Input**: s = "aaabaaa", k = 3

**Output**: true

**Explanation**:

The substring s[4..6] == "aaa" satisfies the conditions.

It has a length of 3.
All characters are the same.
The character before "aaa" is 'b', which is different from 'a'.
There is no character after "aaa".

**Example 2**:

**Input**: s = "abc", k = 2

**Output**: false

**Explanation**:

There is no substring of length 2 that consists of one distinct character and satisfies the conditions.

**Constraints**:

- `1 <= k <= s.length <= 100`
- `s` consists of lowercase English letters only

# Intuition

The problem requires finding a special substring of length `k` that:

1. Contains only **one distinct character**
2. Has **different surrounding characters** (if they exist)
3. The character must appear **at least `k` times** in the entire string

Key insights that drive the solution:

- **Frequency pre-check**: Characters with total count < k can be immediately discarded
- **Sliding window efficiency**: Checking consecutive characters in a window is optimal for this contiguous requirement
- **Boundary validation**: Simple neighbor checks prevent false positives

# Approach

## Optimized Sliding Window with Pre-filtering

1. **Immediate edge case handling**:
   - Return early if string length < k

2. **Character frequency analysis**:
   - Build a frequency map to identify viable candidates
   - Skip characters that can't form k-length substrings

3. **Window validation**:
   - Slide a window of size k through the string
   - For each candidate starting position:
     - Check if all characters in the window are identical using `all()`
     - Verify boundary characters differ from the window's character

4. **Early termination**:
   - Return immediately when a valid substring is found

# Complexity

- **Time Complexity**:
  - Best case: `O(n)` when all characters have count < k
  - Worst case: `O(nk)` when checking all possible windows (e.g., strings like "aaaaa")
  - Breakdown:
    - Frequency counting: `O(n)`
    - Main sliding window: `O((n-k+1)*k)`

- **Space Complexity**:
  - `O(1)` for fixed-size frequency table (26 lowercase letters)
  - Constant additional space for pointers and checks

## Key Optimization

The `all()` function combined with generator expression provides:

1. **Short-circuit evaluation**: Stops checking at first mismatch
2. **Memory efficiency**: Avoids creating substring copies
3. **Code conciseness**: Replaces explicit loop with single-line validation
