"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output Fizz instead of the number and for the multiples of
five output Buzz. For numbers which are multiples of both three and five output FizzBuzz.

Example:

n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = [""] * n
        for i, s in enumerate(output):
            not_3, not_5 = True, True
            if (i+1) % 3 == 0:
                output[i] += "Fizz"
                not_3 = False
            if (i+1) % 5 == 0:
                output[i] += "Buzz"
                not_5 = False
            if not_3 and not_5:
                output[i] = str(i+1)
        return output


if __name__ == '__main__':
    assert Solution().fizzBuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]

