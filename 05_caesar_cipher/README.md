# Caesar Cipher

## Problem Statement

Write a program that can perform the Caesar cipher for English messages that include both upper- and lowercase characters.

## Description

This program implements the Caesar Cipher encryption technique. It shifts each alphabetic character by a fixed number of positions while preserving uppercase and lowercase letters. Non-alphabetic characters such as spaces and punctuation remain unchanged.

## Algorithm

### Encryption

1. Read the input message.
2. Traverse each character.
3. If the character is uppercase, shift it within 'A'–'Z'.
4. If the character is lowercase, shift it within 'a'–'z'.
5. Leave non-alphabetic characters unchanged.
6. Display the encrypted message.

### Decryption

1. Traverse the encrypted message.
2. Shift each alphabetic character backward by the same value.
3. Leave non-alphabetic characters unchanged.
4. Display the original message.

## Sample Output

```
Original Message : Hello World
Encrypted Message: Khoor Zruog
Decrypted Message: Hello World
```

## Technologies Used

- Python 3