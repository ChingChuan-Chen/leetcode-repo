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
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, math.ceil(math.sqrt(n))):
            if not is_prime[i]:
                continue
            for j in range(i*i, n, i):
                is_prime[j] = False
        return sum(is_prime)


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
