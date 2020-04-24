https://py.checkio.org/en/mission/permutation-index/

Let’s imagine a list of all the permutations of a given set. 
Every item on the list has it’s index (starting from 1). The task is to calculate the permutation index.

You are given a tuple of integers. It represents one of the permutations of the consecutive integers (starting from 0). 
You have to return the permutation index of the tuple.

For example

Input: (1, 2, 0)
All the consecutive permutations are:
(0, 1, 2)
(0, 2, 1)
(1, 0, 2)
(1, 2, 0) !!!
(2, 0, 1)
(2, 1, 0)
Output: 4

Example:

assert permutation_index((2, 0, 1)) == 5
assert permutation_index((2, 1, 3, 0, 4, 5)) == 271
