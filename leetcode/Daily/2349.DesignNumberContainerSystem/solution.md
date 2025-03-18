<!-- @leetcode -->

# Design a Number Container System

Design a number container system that can do the following:

- **Insert** or **Replace** a number at the given index in the system.
- **Return** the smallest index for the given number in the system.

Implement the `NumberContainers` class:

- `NumberContainers()` Initializes the number container system.
- `void change(int index, int number)` Fills the container at index with the number. If there is already a number at that index, replace it.
- `int find(int number)` Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.

**Example 1**:

**Input**
["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"]
[[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]

**Output**
[null, -1, null, null, null, null, 1, null, 2]

**Explanation**
NumberContainers nc = new NumberContainers();
nc.find(10); // There is no index that is filled with number 10. Therefore, we return -1.
nc.change(2, 10); // Your container at index 2 will be filled with number 10.
nc.change(1, 10); // Your container at index 1 will be filled with number 10.
nc.change(3, 10); // Your container at index 3 will be filled with number 10.
nc.change(5, 10); // Your container at index 5 will be filled with number 10.
nc.find(10); // Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
nc.change(1, 20); // Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
nc.find(10); // Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.

**Constraints**:

- `1 <= index, number <= 109`
- At most 105 calls will be made in total to change and find.

# Approach 2: Using Min Heap with Lazy Update

## Intuition

An alternate solution could be to use min heaps (priority queues) for managing the indices associated with each number. Similar to Approach 1, we use maps to manage the relationships between indices and numbers, but instead of keeping the indices in a sorted set, we store them in a priority queue (min heap) to handle the ordering for us in this approach.

We follow a similar structure as Approach 1, with two main maps:

indexToNumbers: This map links each index to the number it holds. It helps verify whether an index is still valid during the find operation.
numberToIndices: Instead of using a sorted set to store indices, we use a min heap (priority queue). The priority queue allows us to efficiently retrieve the smallest index associated with a number, as it automatically keeps the indices sorted.
What makes this approach different is the Lazy Update technique. The term "lazy" refers to the deferred handling of index validity during the find operation, rather than cleaning up indices immediately after a change.

Change Operation (Insertion and Replacement)
Similar to Approach 1, we first update the indexToNumbers map to reflect the new number at the given index. Then, instead of immediately removing any outdated indices, we lazily add the new index to the min heap associated with the new number in numberToIndices.

The key difference here is that we don't bother cleaning up the heap during the change operation. Instead, we defer removing the stale indices until the find operation requires it.

Find Operation (Retrieve Smallest Index)
The Lazy Update technique becomes crucial in the find operation. Here, when we need to retrieve the smallest index for a given number, we check the numberToIndices map. If the number doesn’t exist, we return -1.

If the number does exist, we retrieve the min heap for that number. At this point, we don’t assume that the top element of the heap is necessarily valid. The heap may contain stale indices that are no longer associated with the target number. Instead of removing them immediately, we lazily pop the top element of the heap and check if it still maps to the target number using the indexToNumbers map.

If it does, we return the index. If not, we continue popping the heap until we find a valid index or exhaust the heap. This "lazy" way ensures that the heap is only cleaned up when it's absolutely necessary, avoiding unnecessary operations during the change phase.

For a more comprehensive understanding of heaps and priority queues, check out the Heap Explore Card 🔗. This resource provides an in-depth look at heap-based algorithms, explaining their key concepts and applications with a variety of problems to solidify understanding of the pattern.

## Algorithm

Initialize numberToIndices as an hash map where the key is a number and the value is a min-heap (priority queue) of indices for that number.

Initialize indexToNumbers as a hash map where the key is an index and the value is the corresponding number at that index.

change(index, number):

Update the mapping of indexToNumbers to associate the given index with the new number.
Add the index to the min-heap corresponding to the number in numberToIndices.
find(number):

If the number is not present in numberToIndices, return -1 (indicating the number does not exist).
Retrieve the min-heap (priority queue) associated with the number.
While the min-heap is not empty:
Get the top element (index) of the heap.
If the index corresponds to the target number in indexToNumbers, return that index.
If the index maps to a different number, remove the stale index by popping it from the heap.
If no valid index is found, return -1.


