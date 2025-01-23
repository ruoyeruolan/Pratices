<!-- 
@leetcode

-->

# Solution

## Overview

We are given a grid representing a server center in the form of a matrix of size `m x n`. Each cell of the matrix contains either a `1`, indicating the presence of a server, or a `0`, indicating an empty space.

We need to return the number of servers that can communicate with at least one other server. This excludes servers that are isolated, i.e., those that do not share a row or column with any other server.

The first thing to note is that a server can communicate with another server if they are located either in the same row or the same column. Thus, the key observation here is that we only need to check rows and columns to determine if a server is communicable. If there’s at least one other server in the same row or column, then this server is communicable.

## Approach 1: Brute-Force

### Intuition

We know that each cell either contains a server (represented by `1`) or is empty (represented by `0`). So, we start by going through each cell to see if there is a server at that position. If the current cell contains a server, we then check if this server can communicate with any other server. If it can, we count it as communicable.

Once we find a server, we check if there is any other server in the same row that can communicate with it. We do this by iterating through all the other cells in the same row. If we find another server in the same row, we can immediately mark it as communicable.

If we do not find any other server in the row, we proceed to check the column. We iterate through all the other rows in the same column to see if there is another server. If a server is found in the same column, we know this server can communicate and is communicable.

As soon as we determine that a server can communicate (either in the same row or column), we increment the total communicable servers count. Once we finish checking the entire grid, we return the count of communicable servers.

### Algorithm

- Initialize `numRows` and `numCols` to represent the number of rows and columns in the `grid`.
- Initialize `communicableServersCount` to `0`, which will keep track of the count of communicable servers.
- Traverse through the grid:
  - For each server at position (`row`, `col`) where `grid[row][col] == 1`:
    - Set `canCommunicate` to `false`.
    - Check for communication in the same row:
      - Iterate through each column `otherCol` in the same row:
        - If `otherCol` is not equal to col and `grid[row][otherCol] == 1`, set `canCommunicate` to `true` and break the loop.
    - If `canCommunicate` is true, increment `communicableServersCount`.
    - If no communication was found in the same row, check for communication in the same column:
      - Iterate through each row `otherRow` in the same column:
        - If `otherRow` is not equal to row and `grid[otherRow][col] == 1`, set `canCommunicate` to `true` and break the loop.
        - If `canCommunicate` is t`r`ue, increment `communicableServersCount`.
- Return `communicableServersCount`, the total count of servers that can communicate.

```python
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        communitcabeSeversCount = 0

        for row in range(numRows):
            for col in range(numCols):
                
                if grid[row][col] == 1:
                    canCommunicate = False
                    for otherCol in range(numRows):
                        if grid[otherCol][col] == 1 and otherCol != row:
                            canCommunicate = True
                            break
                    if canCommunicate:
                        communitcabeSeversCount += 1
                    else:
                        for otherRow in range(numCols):
                            if grid[row][otherRow] == 1 and otherRow != col:
                                canCommunicate = True
                                break
                        if canCommunicate:
                            communitcabeSeversCount += 1
        return communitcabeSeversCount
```

### Complexity Analysis

Let `m` be the number of rows and `n` be the number of columns in the `grid`.

- Time complexity: `O(m⋅n⋅(m+n))`
  
  The algorithm traverses through each cell in the `grid` using nested loops, where the outer loop runs `m` times (for each row) and the inner loop runs `n` times (for each column). For each cell containing a server (`grid[row][col] == 1`), it performs two additional checks:
  1. It checks the entire row to see if there is another server in the same row. This involves iterating over `n` columns.
  2. If no server is found in the same row, it checks the entire column to see if there is another server in the same column. This involves iterating over `m` rows.
  3. Since these checks are performed for each server, the worst-case time complexity is `O(m⋅n⋅(m+n))`.

- Space complexity: `O(1)`
  
  The algorithm uses a constant amount of extra space, as it only maintains a few variables (`numRows`, `numCols`, `communicableServersCount`, `canCommunicate`, etc.). No additional data structures are used that scale with the input size. Therefore, the space complexity is `O(1)`.

## Approach 2: Track Using Two Arrays

### Intuition

To optimize the checking process, the first step is to count how many servers exist in each row and each column before we start checking individual servers.

We don’t need to check the entire row and column every time for every server. Instead, we can track the number of servers in each row and column using two arrays: `rowCounts` and `colCounts`. We loop over the `grid` once, and for each server (`grid[row][col] == 1`), we increment the count for the corresponding row and column. This precomputes how many servers are present in each row and column.

The advantage of this approach is that we know in advance how many servers are in a given row or column, so when we encounter a server, we can quickly determine if it’s communicable by checking these precomputed values.

Once we have the counts of servers in each row and column, the next task is to identify which servers are communicable. For a server at position (`row`, `col`), we need to check:

- If the row has more than one server (i.e., `rowCounts[row] > 1`), which means there are other servers in the same row.
- If the column has more than one server (i.e., `colCounts[col] > 1`), which means there are other servers in the same column.
If either condition is true, the server can communicate, and we increment the count of communicable servers.

Once we’ve checked all servers and counted the communicable ones, we simply return the count.

### Algorithm

- Initialize two arrays, `rowCounts` and `colCounts`, of appropriate sizes to keep track of the server counts in each row and column.
- Count servers in each row and column:
  - Iterate through each row (`row`), and for each row, iterate through each column (`col`):
  - If there’s a server at `grid[row][col]`, increment the corresponding values in `rowCounts[row]` and `colCounts[col]`.
- Initialize `communicableServersCount` to `0`, which will store the count of servers that can communicate.
- Count servers that can communicate (i.e., those in the same row or column as another server):
  - Iterate again through each row and column:
          - If there’s a server at grid[row][col], check if it can communicate with another server (i.e., if rowCounts[row] > 1 or colCounts[col] > 1).
            - If so, increment `communicableServersCount`.
- Return `communicableServersCount`, the total count of servers that can communicate.
