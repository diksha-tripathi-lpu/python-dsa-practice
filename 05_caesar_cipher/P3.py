'''Write a program that can perform the Caesar cipher for English messages that include both upper and lowercase characters.'''

class CaesarCipher:

    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, message):
        result = ""

        for ch in message:
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + self.shift) % 26 + ord('A'))
            elif ch.islower():
                result += chr((ord(ch) - ord('a') + self.shift) % 26 + ord('a'))
            else:
                result += ch

        return result

    def decrypt(self, message):
        result = ""

        for ch in message:
            if ch.isupper():
                result += chr((ord(ch) - ord('A') - self.shift) % 26 + ord('A'))
            elif ch.islower():
                result += chr((ord(ch) - ord('a') - self.shift) % 26 + ord('a'))
            else:
                result += ch

        return result


cipher = CaesarCipher(3)

message = "Hello World"

encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("Original Message :", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)