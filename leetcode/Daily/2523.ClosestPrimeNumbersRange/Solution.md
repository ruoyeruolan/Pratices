# 2523. Closest Prime Numbers in Range

Given two positive integers `left` and `right`, find the two integers `num1` and `num2` such that:

- `left <= num1 < num2 <= right`.
- Both `num1` and `num2` are prime numbers.
- `num2 - num1` is the `minimum` amongst all other pairs satisfying the above conditions.

Return the positive integer array `ans = [num1, num2]`. If there are multiple pairs satisfying these conditions, return the one with the **smallest** `num1` value. If no such numbers exist, return `[-1, -1]`.

**Example 1**:

**Input**: left = 10, right = 19

**Output**: [11,13]

**Explanation**: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

**Example 2**:

**Input**: left = 4, right = 6
**Output**: [-1,-1]
**Explanation**: There exists only one prime number in the given range, so the conditions cannot be satisfied.

**Constraints**:

- `1 <= left <= right <= 10^6`


# Solution

## Approach 1: Sieve of Eratosthenes

**Intuition**

We are given two numbers, `left` and `right`, and we need to find a pair of prime numbers within this range such that their difference is minimized. If multiple pairs have the same minimum difference, we return the one with the smallest values. If no such pair exists, we return `[-1, -1]`.

A simple approach would be to iterate through all numbers in this range, check whether each number is prime, store the primes, and then determine the pair with the smallest difference. However, checking if a number is prime requires verifying that it has no divisors other than `1` and itself. A naive way to do this is to test divisibility for all numbers up to `n`, but a more optimized approach would only check divisibility up to sqrt(n). Even with this optimization, the approach remains too slow. Since `right` can be as large as `10^6`, iterating through all numbers and performing a divisibility check for each would still be inefficient, leading to a Time Limit Exceeded (TLE) error.

A much faster way to find all prime numbers up to a given limit is the **Sieve of Eratosthenes**. Instead of checking each number one by one, the sieve marks multiples of each prime in bulk, eliminating the need for repeated divisibility checks.

We start with a list of numbers from `2` to `100`. Notice we skip 1 since it’s not considered a prime. Starting with the smallest prime, `2`, we know it’s prime because it hasn’t been marked yet. So, we keep it. Now, we cross out all multiples of `2` (like `4`, `6`, `8`, etc.) because they’re definitely not prime. The next number that isn’t crossed out is `3`, so we mark it as a prime. Then, we cross out all multiples of `3` (like `6`, `9`, `12`, etc.). We keep going, finding the next unmarked number (which will be `5`), and marking all of its multiples. We do this for 7 as well and continue until we’ve processed all numbers up to the limit.

The beauty of the Sieve of Eratosthenes is that it saves a lot of time by marking off composites in bulk, rather than testing each number individually to see if it’s prime. By the end, any number that’s still unmarked is a prime.

As we proceed, we collect all the numbers in an array `primeNumbers`, where `sieve[prime] = 1`. For any marked (non-prime) number, we could also keep track of the specific prime that marked it, though, for this problem, it’s sufficient to identify which numbers are prime.

Since all values lie between 1 and 1000000, we can iterate through the array, check for the minimum difference between two consecutive primes, and return it as the answer.

## Approach 2: Analyze Distance between twin primes

**Intuition**

To avoid storing the prime numbers while iterating through the range, we can check if the current number is prime or not. If it is, we can store it and take it's difference with the next prime that we find in this range. Observe that the Sieve of Eratosthenes approach cannot be used here, since it uses extra storage to check whether the number is prime or not. The only method `left` is to iterate through the divisors upto `sqrt(number)` and check if the current number is prime or not.

In this approach, we take advantage of a special property of prime numbers known as **twin primes**, which are pairs of prime numbers that differ by exactly 2, such as (3,5), (11,13), and (17,19). Instead of searching through all prime numbers, we can optimize our search by focusing on this pattern.

A key mathematical observation under the given constraints `(1 ≤ L,R ≤ 10^6)` is that for any range `[L, R]` where R - L ≥ 1452, there is always at least one twin prime pair. This means that if the given range is wide enough (at least 1452 numbers long), we can be certain that a twin prime pair exists. Since no two prime numbers can be closer than a twin prime pair (which has a difference of exactly 2), we can immediately return this result without further searching.

However, if the range [L, R] is smaller than 1452 numbers, we cannot rely on this property and must manually find the closest prime pair. To do this, we iterate through the numbers in the range, check which ones are prime, and compute the smallest difference between consecutive primes.

Therefore, we leverage the concept of twin primes to optimize our search for the closest prime pair. Instead of storing all prime numbers and comparing them later, we track only the last encountered prime (`prevPrime`). As we iterate through the range `[left, right]`, if we find a new prime, we calculate the difference between it and `prevPrime`. If the difference is `2`, we instantly return the pair, since no closer pair can exist. This early exit significantly reduces unnecessary iterations, especially in large ranges where twin primes are guaranteed to exist.

To summarize, if no twin prime pair is found initially, we continue searching for the closest prime pair by tracking the smallest difference encountered. However, if the range is greater than `1452`, it is mathematically guaranteed that at least one twin prime pair will exist within it.

```python
class Solution:
    def isPrime(self, num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0:
            return False
        divisor = 3
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 2
        return True

    def closestPrimes(self, left, right):
        prev_prime = -1
        closestA = -1
        closestB = -1
        min_difference = float("inf")

        # Iterate over the range of numbers and find primes
        for candidate in range(left, right + 1):
            if self.isPrime(candidate):
                if prev_prime != -1:
                    difference = candidate - prev_prime
                    if difference < min_difference:
                        min_difference = difference
                        closestA = prev_prime
                        closestB = candidate
                    if difference == 1 or difference == 2:
                        return [prev_prime, candidate]
                prev_prime = candidate

        return [closestA, closestB] if closestA != -1 else [-1, -1]
```