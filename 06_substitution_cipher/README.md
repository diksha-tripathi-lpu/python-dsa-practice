# Substitution Cipher

## Problem Statement

Implement a class, `SubstitutionCipher`, with a constructor that takes a string containing the 26 uppercase letters in an arbitrary order and uses that mapping for encryption. Derive the backward mapping for decryption.

## Description

This program implements a substitution cipher using a custom permutation of the uppercase English alphabet. The constructor creates both forward and backward mappings, allowing messages to be encrypted and decrypted correctly.

## Algorithm

### Encryption

1. Create a forward mapping from the alphabet to the given permutation.
2. Traverse each character of the message.
3. Replace uppercase letters using the forward mapping.
4. Leave other characters unchanged.

### Decryption

1. Create the backward mapping from the forward mapping.
2. Traverse the encrypted message.
3. Replace uppercase letters using the backward mapping.
4. Leave other characters unchanged.

## Sample Output

```
Original Message : HELLO WORLD
Encrypted Message: ITSSG VGKSR
Decrypted Message: HELLO WORLD
```
