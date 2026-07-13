# Card Hand using Positional List

## Problem Statement

Implement a `CardHand` class that represents a player's hand using a single Positional List ADT (implemented as a doubly linked list).

Cards of the same suit are grouped together. The implementation maintains four fingers (one for each suit: Hearts, Clubs, Spades, and Diamonds) to efficiently perform card operations.

## Features

The `CardHand` class supports the following operations:

- **add_card(rank, suit)**  
  Adds a new card while keeping cards of the same suit together.

- **play(suit)**  
  Removes and returns a card of the specified suit. If no such card exists, an arbitrary card is removed and returned.

- **__iter__()**  
  Iterates through all cards currently in the hand.

- **all_of_suit(suit)**  
  Iterates through all cards of the specified suit.

---

## Data Structures Used

- Doubly Linked List
- Positional List ADT
- Dictionary (for maintaining four suit fingers)

---

## Algorithm

1. Implement a Positional List using a Doubly Linked List.
2. Maintain one finger for each suit.
3. If a card of the suit already exists, insert the new card immediately after the last card of that suit.
4. If no card of that suit exists, append the card to the end of the hand.
5. While playing a card, remove the last card of the requested suit using its finger.
6. If the requested suit is unavailable, remove the first available card from the hand.
7. Traverse the list to iterate through all cards or cards of a specific suit.

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| add_card() | O(1) |
| play() | O(1) |
| __iter__() | O(n) |
| all_of_suit() | O(n) |

where **n** is the total number of cards in the hand.

---

## Sample Output

```
Cards in Hand:
AH
7H
2C
10C
KS
5D

Playing Heart:
7H

Cards Left:
AH
2C
10C
KS
5D

All Clubs:
2C
10C
```

---

## Author

**Diksha Tripathi**