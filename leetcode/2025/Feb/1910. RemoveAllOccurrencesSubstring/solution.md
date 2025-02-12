<!-- @leetcode -->

# 1910. Remove All Occurrences of a Substring

Given two strings `s` and `part`, perform the following operation on `s` until all occurrences of the substring `- ` are removed:

- Find the **leftmost** occurrence of the substring part and remove it from `s`.

Return `s` after removing all occurrences of `part`.

A substring is a contiguous sequence of characters in a string.

**Example 1**:

**Input**: s = "daabcbaabcbc", part = "abc"
**Output**: "dab"
**Explanation**: The following operations are done:

- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".

Now s has no occurrences of "abc".

**Example 2**:

**Input**: s = "axxxxyyyyb", part = "xy"
**Output**: "ab"
**Explanation**: The following operations are done:

- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".

Now s has no occurrences of "xy".

**Constraints**:

- `1 <= s.length <= 1000`
- `1 <= part.length <= 1000`
- `s​​​​​​` and `part` consists of lowercase English letters.

# Solution

## Approach 1: Iteration

## Intuition

We are given a string `s` and a substring `part`, and we need to repeatedly remove the first occurrence of part from `s` until it no longer appears. Since the constraints are relatively small (`s.length <= 1000 and part.length <= 1000`), we can try a brute force approach.

We can use a simple iterative approach which loops through `s` as long as `part` is present in it. Each time we find `part`, we need to remove its first occurrence. To do this, we first locate the **leftmost** occurrence of part in `s`. Once we know where it starts, we can break s into three sections: the part of the string before the occurrence of part, the occurrence of part itself, and the part of the string after part. By combining the first and third sections (effectively leaving out the middle section), we remove that occurrence of part from s.

When the loop finishes, `s` will no longer contain any occurrences of part, so we return it as the result.

> **Note** It’s worth noting that we can simplify this process by utilizing built-in string methods provided by the programming language.
> For instance, in Java, the String.replaceFirst method can be used to replace the first occurrence of a substring, in Python3 we can use str.replace, and in C++ we can use a combination of std::string::erase and std::string::find.
> Most of the time, it is beneficial to use these built-in functions since they are heavily optimized and tested, and will almost always perform better than our own implementations.

## Algorithm

- Run a `while` loop to repeatedly check if the string `s` contains the substring `part`.
  - Find the index of the **leftmost** occurrence of part in s and store it in a variable `partStartIndex`.
  - Use the substring method to extract the portion of s before part (`s.substring(0, partStartIndex)`) and the portion after part (`s.substring(partStartIndex + part.length())`).
  - Concatenate the first and last portions and assign it back to s.

- Return the updated string s, which no longer contains any occurrences of part.

```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Continue removing occurrences of 'part' as long as it exists in 's'
        while part in s:
            # Find the index of the leftmost occurrence of 'part'
            part_start_index = s.find(part)

            # Remove the substring 'part' by concatenating segments before and after 'part'
            s = s[:part_start_index] + s[part_start_index + len(part) :]

        # Return the updated string after all occurrences are removed
        return s
```

## Approach 2: Stack

### Intuition

In the first approach, we relied on built-in methods to find and remove substrings. Let’s explore how to implement this functionality entirely on our own.

One issue with repeatedly removing substrings from a string is that it requires recreating the entire string every time. We need a way such that removing the substring characters from a string at any point is as close to constant time as possible.

We can simulate this using a stack. A stack allows us to remove its topmost element in constant time. So, if we incrementally put the characters of s in the stack, the moment we find out that the last part of the stack forms part, we simply pop the entire substring out. This means we needed to only loop over the length of part, rather than the entire string s.

To implement this, we can loop over each character of s and add it to the stack. As we add characters, we constantly check if the most recent portion of the stack matches the substring part. If it does, we remove those characters from the stack. This approach avoids scanning the entire string repeatedly and only focuses on the portions of s that could potentially contain part.

However, if at any point the characters don’t match, it means that the stack doesn’t contain part at the top. In that case, any intermediate pops made during the check need to be undone, so the characters are pushed back onto the stack in the correct order. The process continues for the rest of the string.

When we finish processing all the characters in s, the stack will contain the modified version of s with all occurrences of part removed. At this point, the stack’s contents are reversed compared to the original string, so we reverse them back to produce the final result, which is then returned.

For a more comprehensive understanding of stacks, check out the Stack Explore Card 🔗. This resource provides an in-depth look at stacks, explaining their key concepts and applications with a variety of problems to solidify understanding of the pattern.

### Algorithm

Initialize a stack of characters stk to store the characters of the string as they are processed.
Calculate the lengths of the input string s and the substring part, storing them in strLength and partLength, respectively.
Use a for loop to iterate through each character in the string s, starting from index 0 and ending at strLength - 1.
Push the current character of the string onto the stack.
Check if the size of the stack is greater than or equal to partLength. If so:
Use the helper method checkMatch to check if the top of the stack matches part:
If a match is found, pop the top partLength characters from the stack.
After processing the entire string, initialize a string result to construct the resulting string.
While the stack is not empty, pop each character from the stack and append it to the result.
Reverse the order of result to correct the sequence of characters and return it.
Helper method checkMatch(stk, part, partLength):

Initialize a temporary stack temp and copy all characters from the original stack stk into temp.
Use a for loop to iterate over part in reverse order, starting from index partLength - 1 and ending at 0. For each character:
Compare the current character of part with the top character of temp:
If they do not match, return false.
Else, remove the top character from temp.
If all characters of part match the top characters of the stack in reverse order, return true.

```python
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)

        # Iterate through each character in the string
        for char in s:
            # Push current character to stack
            stack.append(char)

            # If stack size is greater than or equal to the part length, check for match
            if len(stack) >= part_length and self._check_match(
                stack, part, part_length
            ):
                # Pop the characters matching 'part' from the stack
                for _ in range(part_length):
                    stack.pop()

        # Convert stack to string with correct order
        return "".join(stack)

    # Helper function to check if the top of the stack matches the 'part'
    def _check_match(self, stack: list, part: str, part_length: int) -> bool:
        # Compare the top 'part_length' elements of the stack with 'part'
        return "".join(stack[-part_length:]) == part
```