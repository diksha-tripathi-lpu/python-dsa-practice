"""Implement a CardHand class that supports a person arranging a group of cards in his or her 
hand. The simulator should represent the sequence of cards using a single positional list 
ADT so that cards of the same suit are kept together. Implement this strategy by means of 
four “fingers” into the hand, one for each of the suits of hearts, clubs, spades, and diamonds, 
so that adding a new card to the person’s hand or playing a correct card from the hand can 
be done in constant time.  
The class should support the following methods:  
● add_card(r, s): Add a new card with rank r and suit s to the hand. 
● play(s): Remove and return a card of suit s from the player’s hand; if there is no card 
of suit s, then remove and return an arbitrary card from the hand.  
● __iter__(): Iterate through all cards currently in the hand.  
● all_of_suit(s): Iterate through all cards of suit s that are currently in the hand"""



class _DoublyLinkedBase:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None  # Deprecate node
        return element


class PositionalList(_DoublyLinkedBase):

    class Position:
        __slots__ = '_container', '_node'

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:  # Deprecated node check
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    # Accessors
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # Mutators
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)


class Card:
    __slots__ = '_rank', '_suit'

    SUITS = ('H', 'C', 'S', 'D')  # Hearts, Clubs, Spades, Diamonds

    def __init__(self, rank, suit):
        if suit not in Card.SUITS:
            raise ValueError(f'Invalid suit: {suit}')
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __repr__(self):
        return f'{self._rank}{self._suit}'


class CardHand:
  
    def __init__(self):
        self._L = PositionalList()
        # Four fingers: each stores the Position of the LAST card
        # in that suit's contiguous group (or None if no cards of that suit exist).
        self._fingers = {s: None for s in Card.SUITS}

    def __len__(self):
        return len(self._L)

    def add_card(self, r, s):
        card = Card(r, s)
        finger = self._fingers[s]

        if finger is None:
            # First card of this suit: append to end of list
            new_pos = self._L.add_last(card)
        else:
            # Insert directly after the last card of this suit
            new_pos = self._L.add_after(finger, card)

        # Update finger to point to the newly inserted card
        self._fingers[s] = new_pos

    def play(self, s):
       
        finger = self._fingers[s]

        if finger is not None:
            # Find the position before deleting (so we don't inspect a deleted node)
            prev_pos = self._L.before(finger)
            removed_card = self._L.delete(finger)

            # Update the finger: if the predecessor is of the same suit, it becomes the new finger
            if prev_pos is not None and prev_pos.element().suit == s:
                self._fingers[s] = prev_pos
            else:
                self._fingers[s] = None

            return removed_card

        # Fallback: remove arbitrary card (the first card in hand)
        first_pos = self._L.first()
        if first_pos is None:
            raise IndexError('Cannot play from an empty hand')

        removed_card = first_pos.element()
        removed_suit = removed_card.suit

        # If the card being removed happens to be a finger for its suit, clear/update it
        if self._fingers[removed_suit] == first_pos:
            self._fingers[removed_suit] = None

        self._L.delete(first_pos)
        return removed_card

    def __iter__(self):
        for card in self._L:
            yield card

    def all_of_suit(self, s):
        for card in self._L:
            if card.suit == s:
                yield card


if __name__ == "__main__":
    hand = CardHand()

    # Add cards
    hand.add_card("A", "H")
    hand.add_card("7", "H")
    hand.add_card("2", "C")
    hand.add_card("10", "C")
    hand.add_card("K", "S")
    hand.add_card("5", "D")

    print("Cards in Hand:")
    print([str(c) for c in hand])

    print("\nPlaying Heart:")
    print(hand.play("H"))

    print("\nCards Left:")
    print([str(c) for c in hand])

    print("\nAll Clubs:")
    print([str(c) for c in hand.all_of_suit("C")])