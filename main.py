import wave


def read_sound_file(filename):
    with wave.open(filename, 'rb') as file:
        params = file.getparams()
        sound_data = file.readframes(params.nframes)
    return params, sound_data


def write_sound_file(filename, params, data):
    with wave.open(filename, 'wb') as file:
        file.setparams(params)
        file.writeframes(data)


def swap(x, y):
    x, y = y, x


def key_scheduling_algorithm(key, state_vector):
    temp_vector = []
    j = 0

    for i in range(len(state_vector)):
        temp_vector.append(key[i % len(key)])

    for i in range(len(state_vector)):
        j = (j + state_vector[i] + temp_vector[i]) % len(state_vector)
        swap(state_vector[i], state_vector[j])


def pseudo_random_generation_algorithm(sound_data, state_vector, cipher):
    i, j = 0, 0
    modified_state_vector = state_vector.copy()

    for byte in sound_data:
        i = (i + 1) % len(modified_state_vector)
        j = (j + modified_state_vector[i]) % len(modified_state_vector)
        swap(modified_state_vector[i], modified_state_vector[j])
        t = (modified_state_vector[i] + modified_state_vector[j]) % len(modified_state_vector)
        k = modified_state_vector[t]
        encrypted_byte = byte ^ k
        cipher.append(encrypted_byte)


def encrypt(sound_data, key, state_vector):
    key_scheduling_algorithm(key, state_vector)
    cipher = bytearray()
    pseudo_random_generation_algorithm(sound_data, state_vector, cipher)
    return bytes(cipher)


def decrypt(cipher, key, state_vector):
    return encrypt(cipher, key, state_vector)  # RC4 encryption and decryption are the same operation


def main():
    key = "0123456789ABCDEF"  # input("Enter the key: ")
    if len(key) != 16:
        return print("Key must be 16 characters long.")

    # Read the sound file
    filename = "input.wav"
    params, sound_data = read_sound_file(filename)

    # Convert key and sound data to lists of integers
    key = [ord(char) for char in key]

    # Initialize the state vector
    state_vector = list(range(0, 256))

    # Encrypt the sound file
    encrypted_sound_data = encrypt(sound_data, key, state_vector)

    # Write the encrypted sound file
    encrypted_filename = "encrypted.wav"
    write_sound_file(encrypted_filename, params, encrypted_sound_data)
    print("Encryption completed.")

    # Decrypt the encrypted sound file
    decrypted_sound_data = decrypt(encrypted_sound_data, key, state_vector)

    # Write the decrypted sound file
    decrypted_filename = "decrypted.wav"
    write_sound_file(decrypted_filename, params, decrypted_sound_data)
    print("Decryption completed.")


if __name__ == "__main__":
    main()
