
# 3306. Count of Substrings Containing Every Vowel and K Consonants II

You are given a string `word` and a non-negative integer `k`.

Return the total number of substrings of word that contain every vowel (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) at least once and exactly `k` consonants.

**Example 1**:

**Input**: word = "aeioqq", k = 1

**Output**: 0

**Explanation**:

There is no substring with every vowel.

**Example 2**:

**Input**: word = "aeiou", k = 0

**Output**: 1

**Explanation**:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

**Example 3**:

**Input**: word = "ieaouqqieaouqq", k = 1

**Output**: 3

**Explanation**:

The substrings with every vowel and one consonant are:

- word[0..5], which is "ieaouq".
- word[6..11], which is "qieaou".
- word[7..12], which is "ieaouq".

**Constraints**:

- `5 <= word.length <= 2 * 105`
- word consists only of lowercase English letters.
- `0 <= k <= word.length - 5`

# Solution

## Overview

Given a string `word` and an integer `k`, we need to find the total number of substrings of word that satisfy two requirements:

- The substring must contain every vowel `(a, e, i, o, u)`. Each vowel can appear **any number of times** in the substring.
- The substring must have exactly `k` consonants (any character that is not a vowel).

This type of problem is common in substring and subarray searches, where we look for all occurrences that meet a specific set of constraints. Some related problems include:

> `3.` Longest Substring Without Repeating Characters
> `2461.` Maximum Sum of Distinct Subarrays With Length K

Since we are dealing with substrings and need to enforce specific constraints efficiently, we can use the sliding window technique, which allows us to dynamically adjust the window size while keeping track of the required conditions.

## Approach 1: Sliding Window

### Intuition

A brute force approach would involve manually going through every substring of word and checking if each substring satisfies the 2 requirements listed. However, this is inefficient because it repeatedly processes overlapping substrings. Instead of looking at every possible substring, we can use a sliding window to track and update information dynamically as we scan through word.

Our sliding window maintains two pointers, start and end, to define the starting and ending index of the current substring. The window expands by moving end forward and shrinks by moving start forward as we search for all occurrences of a valid substring. We can keep a `numValidSubstrings` variable to count the total number of valid substrings we see in our window.

To determine if a window contains a valid substring, we track two values:

- `vowelCount`: A frequency map storing how many times each vowel appears in the window.
- `consonantCount`: A counter tracking the number of consonants in the window.

Our window would contain a valid substring when `vowelCount` contains all five vowels and `consonantCount` is exactly `k`.

At the start, our window is empty. As we iterate through word, we expand the window by adding the current character at end. If it is a vowel, we update vowelCount. If it is a consonant, we increase consonantCount. As we expand there are 3 possible cases:

- `consonantCount < k` or `vowelCount` doesn't have all vowels yet: This will happen in the early iterations of the sliding window process when the window is still small. In this case, we don't have to make adjustments and can continue expanding.

- `consonantCount > k`: If `consonantCount` becomes too large, we need to shrink our window by moving start forward and removing elements from the beginning. As we remove each element, we adjust `consonantCount` and `vowelCount` accordingly. Once a vowel's count goes to 0, we remove it from `vowelCount`. Once the window is back within valid constraints, we resume expanding.

- `consonantCount == k` and `vowelCount` contains all vowels: This means we have found a window with a valid substring. Let's consider how we can adjust our substring to find more valid substrings.
  - Expanding: If we expand to another vowel, we know that this new substring is also valid. If the new character is a consonant, `consonantCount` exceeds `k` and we no longer have a valid substring. Thus, we can continue expanding our end boundary to find new substrings until we encounter a consonant. Precisely, if the next consonant is at index `nextConsonantIndex`, then we have a total of `nextConsonantIndex` - end new valid substrings. Instead of manually iterating to find the next consonant each time, we can precompute an array `nextConsonant`, where `nextConsonant[i]` stores the index of the next consonant after index `i`. With this, we can quickly determine how many new valid substrings can be formed from any valid window.
  - Shrinking: We can find more valid substrings by shrinking our window until we no longer have a valid substring. For each new shrunken window, we can reapply the expanding logic discussed above, and create `nextConsonant[end] - end` new windows.

In summary, when we come across a valid window, we can keep shrinking while the window is still valid. For each shrunken window, we have nextConsonant - end more valid windows.

After we have iterated through all characters of word, we have successfully found all valid substrings.

### Algorithm

- Initialize `numValidSubstrings = 0` to count total number of valid substrings.
- Initialize `start = 0` and `end = 0` to represent the start and end of our sliding window.
- Initialize map `vowelCount` to keep track of the frequency of the 5 vowels in our sliding window.
- Initialize `consonantCount` to keep track of the number of consonants in our sliding window.
- Initialize array `nextConsonant` to hold the index of next consonant for all indices.
- Create helper function `isVowel(char c)` to return whether or not a character is a vowel
- Populating nextConsonant:
  - We initialize `nextConsonantIndex` to a default value of `word.length()`
  - We iterate through word backwards using `i = word.length() - 1` to index. For each i:
    - `nextConsonant[i] = nextConsonantIndex`.
    - If `word[i]` is a consonant (`isVowel(word[i]) == false`), update `nextConsonantindex = i`.
- Start the sliding window process. While `end < word.length()`:
  - Get new letter: `newLetter = word[end]`.
  - Update counts with the new letter:
    - If `isVowel(newLetter)`, then increment corresponding frequency in `vowelCount`.
    - Otherwise, increment `consonantCount`: `consonantCount++`.
  - While `consonantCount` > `k`, shrink our window:
    - Get first letter in window: startLetter = word[start].
    - Remove it from the window:
      - If isVowel(startLetter), then decrement corresponding frequency in vowelCount. If the frequency reaches 0, delete startLetter from vowelCount.
      - Otherwise, decrement consonantCount: consonantCount--.
      - Shrink the window by 1: start++.
  - While we have a valid window, keep shrinking and count the total number of valid substrings found:
    - Add nextConsonant[end] - end to numValidSubstrings. This is the total number of valid substrings with the given start.
    - Get first letter in window: startLetter = word[start].
    - Remove it from the window:
    - If isVowel(startLetter), then decrement corresponding frequency in vowelCount. If the frequency reaches 0, delete startLetter from vowelCount.
    - Otherwise, decrement consonantCount: consonantCount--.
    - Shrink the window by 1: start++.
  - Increment end to add the next character to our window: end++

```python
class Solution:
    def _isVowel(self, c: str) -> bool:
        return c == "a" or c == "e" or c == "i" or c == "o" or c == "u"

    def countOfSubstrings(self, word: str, k: int) -> int:
        num_valid_substrings = 0
        start = end = 0
        vowel_count = {}  # Dictionary to keep counts of vowels
        consonant_count = 0  # Count of consonants
        next_consonant = [0] * len(
            word
        )  # Array to compute index of next consonant for all indices
        next_consonant_index = len(word)

        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if not self._isVowel(word[i]):
                next_consonant_index = i

        while end < len(word):
            new_letter = word[end]
            if self._isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            while (
                consonant_count > k
            ):  # Shrink window if too many consonants are present
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            while (
                start < len(word)
                and len(vowel_count) == 5
                and consonant_count == k
            ):  # Try to shrink if window is valid
                num_valid_substrings += next_consonant[end] - end
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            end += 1

        return num_valid_substrings
```

## Approach 2: Sliding Window (Relaxed Constraints)

### Intuition_

In the previous approach, we adjusted our sliding window by strictly following the 2 constraints:

- A valid window must contain all vowels.
- A valid window must contain exactly `k` consonants.

The second requirement introduces more complexity to our sliding window solution, leading us to precompute a `nextConsonant` array to keep track of when the next consonant occurs for all indices in the string. To simplify the problem, let's relax this second constraint, so that valid substrings have at least `k` consonants instead.

Let’s say we find a window (substring) that contains all vowels and exactly `k` consonants. What happens if we keep expanding the window to the right?

- Adding more characters will never remove a vowel from the window.
- It may add more consonants, but since we only need at least k, the window remains valid.

**This means that once we reach our first valid window (where end is the right boundary of the window), every substring that extends from this point onward is also valid**. Instead of checking each one individually, we can instantly count them:

`New valid substrings=word.length−end`

After counting these substrings, we shrink the window from the left (start index) and repeat the process, making sure our window remains valid.

Now, the question is how we can connect this relaxed version of the problem back to the original problem. Let's denote the solution to this relaxed problem with a given `word` and `k` as `atLeastK(word, k)`. The key observation is the number of valid substrings (with exactly `k` consonants) is equal to `atLeastK(word, k) - atLeastK(word, k + 1)`.

With this problem reduction, we can simplify our sliding window approach and eliminate the need for an auxiliary data structure to keep track of occurrences of consonants.

### Algorithm_

- Create helper function `isVowel(char c)` to return whether or not a character is a vowel.
- Create helper function `atLeastK(word, k)`:
- Initialize `numValidSubstrings = 0` to count total number of valid substrings.
- Initialize `start = 0` and `end = 0` to represent the start and end of our sliding window.
- Initialize map `vowelCount` to keep track of the frequency of the 5 vowels in our sliding window.
- Initialize `consonantCount` to keep track of the number of consonants in our sliding window.
- Start the sliding window process. While `end < word.length()`:
  - Get new letter: `newLetter = word[end]`.
  - Update counts with the new letter:
    - If `isVowel(newLetter)`, then increment corresponding frequency in `vowelCount`.
    - Otherwise, increment `consonantCount`: `consonantCount++`.
  - While `vowelCount.size() == 5 && consonantCount >= k`:
    - Count the valid substrings: `numValidSubstrings += word.length() - end`.
    - Get first letter in window: `startLetter = word[start]`.
    - Remove it from the window:
      - If `isVowel(startLetter)`, then decrement corresponding frequency in `vowelCount`. If the frequency reaches 0, delete `startLetter` from `vowelCount`.
      - Otherwise, decrement `consonantCount`: `consonantCount--`.
      - Shrink the window by `1`: `start++`.
    - Increment end to add the next character to our window: end++.
- Return `atLeast(word, k) - atLeast(word, k + 1)`.
  
```python
class Solution:
    def _isVowel(self, c: str) -> bool:
        return c in ["a", "e", "i", "o", "u"]

    def _atLeastK(self, word: str, k: int) -> int:
        num_valid_substrings = 0
        start = 0
        end = 0
        # keep track of counts of vowels and consonants
        vowel_count = {}
        consonant_count = 0

        # start sliding window
        while end < len(word):
            # insert new letter
            new_letter = word[end]

            # update counts
            if self._isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            # shrink window while we have a valid substring
            while len(vowel_count) == 5 and consonant_count >= k:
                num_valid_substrings += len(word) - end
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] = (
                        vowel_count.get(start_letter) - 1
                    )
                    if vowel_count.get(start_letter) == 0:
                        vowel_count.pop(start_letter)
                else:
                    consonant_count -= 1
                start += 1

            end += 1

        return num_valid_substrings

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._atLeastK(word, k) - self._atLeastK(word, k + 1)
```