from collections import Counter
from typing import List, Union

Number = Union[int, float]

def find_unique_value(nums: List[Number]) -> Number:
    for n, c in Counter(nums).items():
        if c == 1:
            return n


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")