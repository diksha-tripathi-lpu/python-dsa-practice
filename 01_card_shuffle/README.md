# Card Shuffle

## Problem Statement

Given a list containing 2n elements, divide it into two equal halves and shuffle the list by alternately taking elements from each half.

### Example

Input
```
1 2 3 4 5 6 7 8
```

Output
```
1 5 2 6 3 7 4 8
```

## Algorithm

1. Divide the list into two equal halves.
2. Store them in L1 and L2.
3. Create a new list.
4. Append one element from L1 followed by one element from L2.
5. Repeat until all elements are merged.
