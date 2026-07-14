'''Implement a class, SubstitutionCipher, with a constructor that takes a string with the 26 uppercase letters in an arbitrary order and uses that for the forward mapping for encryption. You should derive the backward mapping from the forward version.'''

class SubstitutionCipher:

    def __init__(self, mapping):

        self.forward = {}
        self.backward = {}

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for i in range(26):
            self.forward[alphabet[i]] = mapping[i]
            self.backward[mapping[i]] = alphabet[i]

    def encrypt(self, message):

        result = ""

        for ch in message:
            if ch.isupper():
                result += self.forward[ch]
            else:
                result += ch

        return result

    def decrypt(self, message):

        result = ""

        for ch in message:
            if ch.isupper():
                result += self.backward[ch]
            else:
                result += ch

        return result


mapping = "QWERTYUIOPASDFGHJKLZXCVBNM"

cipher = SubstitutionCipher(mapping)

message = "HELLO WORLD"

encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("Original Message :", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)