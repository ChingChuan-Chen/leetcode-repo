"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        # Only odd numbers are considered (halve the space!)
        sieve = [True] * (n // 2)
        sieve[0] = False  # 1 is not prime

        # Only need to check odd i from 3 to sqrt(n)
        for i in range(3, int(n ** 0.5) + 1, 2):
            if sieve[i // 2]:
                # Start from i*i, mark every i-th odd index as False
                sieve[i * i // 2: (n // 2): i] = [False] * len(sieve[i * i // 2: (n // 2): i])
        return sum(sieve) + 1


if __name__ == '__main__':
    assert Solution().countPrimes(0) == 0
    assert Solution().countPrimes(1) == 0
    assert Solution().countPrimes(2) == 0
    assert Solution().countPrimes(3) == 1
    assert Solution().countPrimes(5) == 2
    assert Solution().countPrimes(7) == 3
    assert Solution().countPrimes(8) == 4
    assert Solution().countPrimes(10) == 4
    assert Solution().countPrimes(11) == 4
    assert Solution().countPrimes(12) == 5
    assert Solution().countPrimes(13) == 5
    assert Solution().countPrimes(14) == 6
    assert Solution().countPrimes(96) == 24
    assert Solution().countPrimes(97) == 24
    assert Solution().countPrimes(98) == 25
    assert Solution().countPrimes(100) == 25
