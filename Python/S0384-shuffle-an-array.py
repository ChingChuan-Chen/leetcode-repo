"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
import random
from typing import List
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        self.array = self.nums.copy()
        for i in range(len(self.array)):
            swap_idx = random.randint(0, len(self.array)-1)
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


if __name__ == '__main__':
    obj = Solution([1, 2, 3])
    assert obj.reset() == [1, 2, 3]
    obj.shuffle()
