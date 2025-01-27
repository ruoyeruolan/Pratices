<!-- @leetcode -->

# Problem

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you **must** take course ai first if you want to take course bi.

For example, the pair `[0, 1]` indicates that you have to take course `0` before you can take course `1`.
Prerequisites can also be **indirect**. If course `a` is a prerequisite of course `b`, and course `b` is a prerequisite of course `c`, then course `a` is a prerequisite of course `c`.

You are also given an array `queries` where `queries[j] = [uj, vj]`. For the `jth` query, you should answer whether course `uj` is a prerequisite of course `vj` or not.

Return a boolean array `answer`, where `answer[j]` is the answer to the `jth` query.

## Example 1:

![Course1](./static/courses4-1-graph.jpg)

Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

## Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.

## Example 3:

![Course3](./static/courses4-3-graph.jpg)

Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

## Constraints:

- `2 <= numCourses <= 100`
- `0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi <= numCourses - 1`
- `ai != bi`
- All the pairs `[ai, bi]` are unique.
- The prerequisites graph has no cycles.
- `1 <= queries.length <= 104`
- `0 <= ui, vi <= numCourses - 1`
- `ui != vi`

# Solution

## Overview

We are given a directed graph representing course dependencies. The graph consists of `numCourses` nodes (denoted as `N` for simplicity) and `E` directed edges, where each edge is represented as a pair `(u, v)`. An edge `(u, v)` indicates that course `u` is a prerequisite for course `v`.

Additionally, we are given `Q` queries. Each query is a pair `(u, v)`, and the goal is to determine if course `u` is a prerequisite for course `v`. The answer to each query should be `true` if `u` is a prerequisite of `v`, and `false` otherwise.

## Approach 3: Topological Sort - Kahn's Algorithm

### Intuition

We need to find a way to process nodes in the correct order, ensuring that each node is processed only after its dependencies are handled. This is where [topological sorting](https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/) comes into play. Kahn’s algorithm is a great fit for this task because it respects the dependencies of each node, ensuring nodes are only visited once their prerequisites are completed.

> **Note**: Topological sorting is an algorithm used in directed graphs to arrange nodes such that for every directed edge from node u to node v, node u comes before v. This is a natural approach when dealing with dependencies, like in project scheduling, task ordering, or handling prerequisites.

Now, to adapt Kahn's algorithm to our needs, we need to keep track of a node’s prerequisites. Instead of just processing nodes in topological order, we'll modify the algorithm to maintain a list of dependencies for each node. As we move from node u to node v, we’ll add all of u's prerequisites to v's prerequisites. This is important because it computes the transitive closure, meaning we’re not just tracking immediate dependencies, but also indirect ones.

By the end of this process, each node will have a complete list of all nodes that must be visited before it. With this setup, when we need to answer a query `(u, v)`, all we have to do is check if `u` is in the list of prerequisites for `v`.

The general structure of Kahn’s algorithm stays the same. We start by calculating the indegree of each node, which tells us how many nodes depend on it. Nodes with an indegree of zero are independent and can be processed first, so we enqueue them. Then, using a queue, we dequeue nodes, process their neighbors, update the prerequisite lists, and enqueue any neighbors whose indegree drops to zero. This continues until we’ve processed all nodes, ensuring the correct order of traversal.

### Algorithm

1. Create an adjacency list (`adjList`) to store the directed graph representing course dependencies.

2. Initialize an array (`indegree`) to track the number of prerequisites (in-degree) for each course.

3. Iterate over the prerequisites array to populate the adjacency list and update the `indegree` for each course.

4. Initialize a queue (`q`) to process courses with zero in-degree (no prerequisites).

5. While the queue is not empty:
   - Dequeue a course (node).
     - For each adjacent course (adj) in the adjacency list of nodes, add the prerequisites of node to the list `nodePrerequisites[adj]`.
   - Decrement the in-degree of the node `adj`, and if the in-degree becomes zero, enqueue it for further processing.
6. For each query `(u, v)`, check if course `u` is in the prerequisite list of course `v` by checking `nodePrerequisites[v]`.

```python
class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodePrerequisites = defaultdict(set)

        while q:
            node = q.popleft()

            for adj in adjList[node]:
                # Add node and prerequisite of the node to the prerequisites of adj
                nodePrerequisites[adj].add(node)
                for prereq in nodePrerequisites[node]:
                    nodePrerequisites[adj].add(prereq)

                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        answer = []
        for q in queries:
            answer.append(q[0] in nodePrerequisites[q[1]])

        return answer
```

### Complexity Analysis

Let `N` be the number of courses (`numCourses`) and let `Q` be the size of the queries list. In the worst case, the size of the prerequisites list can grow up to  $\frac{N(N - 1)}{2}$, when every course is a prerequisite for every other course, forming a complete directed graph.

- Time complexity: O($N^3$ + Q).
  Creating the adjacency list adjList takes O($N^2$) time as we need to iterate over the list prerequisites. The array indegree will be of size O(N). In Kahn's algorithm, we iterate over each node and edge of the vertex which is O($N^2$) and for each edge traversed we will also add the prerequisites to the next node which is another `O(N)`. To answer each query we need constant time to retrieve from the map and hence it's `O(Q)` to answer all queries. Hence, the total time complexity equals O(N^3 + Q).

- Space complexity: O($N^2$).
  List adjList takes O($N^2$) as it will store every edge in the list prerequisites. Array indegree will take `O(N)` space and the queue for Kahn's algorithm will also be `O(N)` size. Map nodePrerequisites will be from the node to its prerequisites and thus the total number of entries can be equal to O($N^2$). Hence the total space complexity equals O($N^2$).

## Approach 4: Floyd Warshall Algorithm

### Intuition

In the first approach, we discussed the concept of transitive closure, which simplified the problem. The key insight was that the transitive closure allows us to determine if a path exists between two nodes, even indirectly. This concept is central to solving the **All-Pairs Shortest Path (APSP)** problem, for which the **Floyd-Warshall algorithm** is commonly used. This algorithm works by systematically considering every possible intermediate node and checking if a path between two nodes can be improved by going through that intermediate node. It then updates the shortest distance between the nodes.

For our problem, however, we don't need to calculate the shortest path, just **whether a path exists**. This leads us to a simple modification of the **Floyd-Warshall algorithm**: instead of keeping track of distances, we’ll use boolean values to represent whether a path exists between two nodes.

The main idea is to check if there’s a path from src to target by looking at all possible intermediate nodes. For each intermediate node, we check if there’s a path from src to that node and a path from that node to target. If both conditions hold, then we can confirm that a path exists between src and target. We then set `isPrerequisite[src][target]` to `true`.

At the end of this process, we’ll have a 2D array, `isPrerequisite`, where each entry `isPrerequisite[u][v]` tells us whether `u` is a prerequisite for `v`.

### Algorithm for Floyd-Warshall

1. Initialize a 2D boolean array `isPrerequisite` of size `numCourses x numCourses` to track direct prerequisite relationships between courses.
2. Populate the `isPrerequisite` matrix based on the prerequisites:
   - For each pair in prerequisites, mark `isPrerequisite[edge[0]][edge[1]]` as `true` to indicate that `edge[0]` is a prerequisite for `edge[1]`.
3. Compute transitive closure of the prerequisite relationships using the Floyd-Warshall algorithm:
   - For each possible intermediate course `intermediate`:
     - For each source course `src`:
       - For each target course `target`:
         - Update `isPrerequisite[src][target]` to include indirect relationships:
           - If `src` can reach intermediate and intermediate can reach target, then `src` can reach target.
4. Initialize an empty list `answer` to store the results of the queries.
5. For each `query` in queries:
   - Add the value of `isPrerequisite[query[0]][query[1]]` to the answer list, indicating whether `query[0]` is a prerequisite for `query[1]`.
6. Return the `answer` list containing the results for all queries.

```python
class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]

        for edge in prerequisites:
            isPrerequisite[edge[0]][edge[1]] = True

        for intermediate in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    # If there is a path src -> intermediate and intermediate -> target, then src -> target exists as well
                    isPrerequisite[src][target] = isPrerequisite[src][
                        target
                    ] or (
                        isPrerequisite[src][intermediate]
                        and isPrerequisite[intermediate][target]
                    )

        answer = []
        for query in queries:
            answer.append(isPrerequisite[query[0]][query[1]])

        return answer
```

### Complexity Analysis

- Time complexity: O($N^3$ + Q).
- Space complexity: O($N^2$).
