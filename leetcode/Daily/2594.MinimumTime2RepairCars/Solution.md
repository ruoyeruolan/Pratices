
# 2594. Minimum Time to Repair Cars

You are given an integer array `ranks` representing the ranks of some mechanics. `ranks_i` is the rank of the `i_th` mechanic. A mechanic with a rank `r` can repair `n` cars in `r * n^2` minutes.

You are also given an integer `cars` representing the total number of cars waiting in the garage to be repaired.

Return **the minimum time** taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

**Example 1**:

**Input**: ranks = [4,2,3,1], cars = 10

**Output**: 16

**Explanation**: 

- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

**Example 2**:

**Input**: ranks = [5,1,8], cars = 6
**Output**: 16
**Explanation**:

- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​

Constraints:

- 1 <= ranks.length <= 10^5
- 1 <= ranks[i] <= 100
- 1 <= cars <= 10^6

# Solution

## Overview

We are given an array `ranks`, where `ranks[i]` represents the efficiency of the `i-th` mechanic. A mechanic with a rank `r` repairs `n` cars in `r * n^2` minutes, meaning the time required increases quadratically as more cars are assigned to a single mechanic. We also have an integer cars, representing the total number of cars that need to be repaired. The goal is to determine the minimum possible time required to repair all cars if all mechanics work simultaneously.

To understand the problem, consider the example where `ranks = [4,2,3,1]` and `cars = 10`. The optimal allocation would be:

- The first mechanic (rank `4`) repairs `2` cars, taking `4 * 2 * 2 = 16` minutes.
- The second mechanic (rank `2`) repairs `2` cars, taking `2 * 2 * 2 = 8` minutes.
- The third mechanic (rank `3`) repairs `2` cars, taking `3 * 2 * 2 = 12` minutes.
- The fourth mechanic (rank `1`) repairs `4` cars, taking 1 * 4 ** 2 = 16 minutes.

Since all mechanics work in parallel, the total time required is determined by the slowest mechanic in the optimal assignment, which is `16` minutes.

The problem essentially boils down to distributing the cars optimally among the mechanics so that the maximum repair time (the slowest mechanic) is minimized. Another way to say this is that a mechanic with a lower rank (higher skill) can repair cars faster than one with a higher rank. A brute force approach of checking every possible distribution would be highly inefficient, so we need a smarter strategy.

A common mistake is misunderstanding how parallel execution works. Instead of focusing on the slowest mechanic, some mistakenly add up all the repair times, as if the tasks were done sequentially. This misinterpretation leads to incorrect conclusions about the total time required.

Another mistake is assuming dynamic programming (DP) is always the right approach for optimization problems. When faced with minimization or maximization, our first instinct might be to reach for DP. However, before committing to it, we need to check the constraints. If the problem lacks overlapping subproblems or an optimal substructure, DP may not be a suitable choice.

## Approach 3: Using Heap

### Intuition

Instead of using binary search, we can directly simulate the car repair process using a min-heap to always prioritize the mechanic who can complete the next repair in the shortest possible time. Since each mechanic follows the formula `time = rank * n^2` to determine how long it takes to repair their `k-th` car, we can predict the sequence of repair times for each mechanic. The first car takes `rank * 1^2 = rank time`, the second car takes `rank * 4 time`, the third car takes `rank * 9 time`, and so on.

Given this pattern, at any moment, the mechanic who will finish the next repair the fastest should be chosen to repair the next car. The most efficient way to track the next available repair time for all mechanics is to use a min-heap, where each entry stores the next repair time for a mechanic, their rank (to calculate future repair times), the number of cars they have already repaired, and the count of mechanics with that rank (since multiple mechanics can have the same rank).

We begin by initializing the heap with the first repair time for each unique rank. If multiple mechanics share the same rank, we keep track of how many exist. Then, we repeatedly extract the mechanic with the earliest repair time and assign them the next car to repair. Once a mechanic repairs a car, we compute their next available repair time using the formula time = rank * (n + 1)^2, then push this new time back into the heap. This process continues until all cars are repaired.

By always selecting the fastest available repair, we ensure that the total time remains minimal while efficiently distributing the workload among mechanics. Since each mechanic’s repair time follows a monotonically increasing pattern, the heap naturally maintains the correct ordering.

```python
class Solution:
    def repairCars(self, rank: List[int], cars: int) -> int:
        # Count the frequency of each rank using a Counter
        count = Counter(rank)

        # Create a Min-heap storing [time, rank, n, count]:
        # - time: time for the next repair
        # - rank: mechanic's rank
        # - n: cars repaired by this mechanic
        # - count: number of mechanics with this rank
        # Initial time = rank (as rank * 1^2 = rank)
        min_heap = [[rank, rank, 1, count[rank]] for rank in count]
        heapify(min_heap)

        # Process until all cars are repaired
        while cars > 0:
            # Pop the mechanic with the smallest current repair time
            time, rank, n, count = heappop(min_heap)

            # Deduct the number of cars repaired by this mechanic group
            cars -= count

            # Increment the number of cars repaired by this mechanic
            n += 1

            # Push the updated repair time back into the heap
            # The new repair time is rank * n^2 (since time increases quadratically with n)
            heappush(min_heap, [rank * n * n, rank, n, count])

        return time
```

> `2560`. House Robber IV
> 
> `875`. Koko Eating Bananas
> 
> `1231`. Divide Chocolate
> 
> `1011`. Capacity To Ship Packages In N Days
> 
> `2587`. Minimum Time to Repair Cars
> 
> `1539`. Kth Missing Positive Number
> 
> `2064`. Minimized Maximum of Products Distributed to Any Store
> 
> `2226`. Maximum Candies Allocated to K Children
> 
> `1802`. Maximum Value at a Given Index in a Bounded Array
> 
> `1482`. Minimum Number of Days to Make m Bouquets
> 
> `1283`. Find the Smallest Divisor Given a Threshold
> 
> `774`. Minimize Max Distance to Gas Station
> 
> `410`. Split Array Largest Sum
