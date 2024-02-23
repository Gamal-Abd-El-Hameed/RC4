from utilites import *


class RC4:
    def __init__(self, key):
        self.key = [ord(char) for char in key]
        self.state_vector = list(range(256))

    def key_scheduling_algorithm(self):
        temp_vector = []
        j = 0
        state_vector_length = len(self.state_vector)

        for i in range(state_vector_length):
            temp_vector.append(self.key[i % len(self.key)])

        for i in range(state_vector_length):
            j = (j + self.state_vector[i] + temp_vector[i]) % state_vector_length
            swap(self.state_vector[i], self.state_vector[j])

    def pseudo_random_generation_algorithm(self, sound_data, cipher):
        i, j = 0, 0
        modified_state_vector = self.state_vector.copy()
        modified_state_vector_length = len(modified_state_vector)

        for byte in sound_data:
            i = (i + 1) % modified_state_vector_length
            j = (j + modified_state_vector[i]) % modified_state_vector_length
            swap(modified_state_vector[i], modified_state_vector[j])
            t = (modified_state_vector[i] + modified_state_vector[j]) % modified_state_vector_length
            k = modified_state_vector[t]
            encrypted_byte = byte ^ k
            cipher.append(encrypted_byte)

    def encrypt(self, sound_data):
        self.key_scheduling_algorithm()
        cipher = bytearray()
        self.pseudo_random_generation_algorithm(sound_data, cipher)
        return bytes(cipher)

    def decrypt(self, cipher):
        return self.encrypt(cipher)  # decryption is the same as encryption
