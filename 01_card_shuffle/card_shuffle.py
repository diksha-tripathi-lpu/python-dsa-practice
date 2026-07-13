"""Describe a method for performing a card shuffle of a list of 
2n elements,by converting it into two lists. A card shuffle 
is a permutation where a list L is cut into two lists, L1 and L2, 
where L1 is the first half of L and L2 is the second half of L, 
and then these two lists are merged into one by taking
the first element in L1, then the first element in L2, 
followed by the second element in L1, the second element in 
L2, and so on."""



def card_shuffle(lst):
    if len(lst) % 2 != 0:
        raise ValueError("List must contain an even number of elements.")
    n = len(lst) // 2

    # Divide the list into two halves
    L1 = lst[:n]
    L2 = lst[n:]

    # Merge alternately
    shuffled = []

    for i in range(n):
        shuffled.append(L1[i])
        shuffled.append(L2[i])

    return shuffled


size = int(input("Enter number of elements (even): "))

if size % 2 != 0:
    print("Number of elements must be even.")
else:
    elements = []

    print("Enter the elements:")
    for _ in range(size):
        elements.append(input())

    result = card_shuffle(elements)

    print("Original List:", elements)
    print("Shuffled List:", result)