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


def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def modify_S_vector(key, S_vector):
    T_vector, j = [], 0
    for i in range(len(S_vector)):
        appe = key[i % len(key)]
        T_vector.append(appe)

    for i in range(len(S_vector)):
        j = (j + S_vector[i] + T_vector[i]) % len(S_vector)
        swap(S_vector, i, j)

    return S_vector


def encrypt(sound_data, S_vector):
    cipher, i, j = bytearray(), 0, 0
    S_vector_mod = S_vector.copy()  # Create copy so the main S_vector is not modified
    for byte in sound_data:
        i = (i + 1) % len(S_vector_mod)
        j = (j + S_vector_mod[i]) % len(S_vector_mod)
        swap(S_vector_mod, i, j)
        t = (S_vector_mod[i] + S_vector_mod[j]) % len(S_vector_mod)
        key_mod = S_vector_mod[t]
        encrypted_byte = byte ^ key_mod
        cipher.append(encrypted_byte)

    return bytes(cipher)


def decrypt(cipher, S_vector):
    return encrypt(cipher, S_vector)  # RC4 encryption and decryption are the same operation


# Main function
def main():
    # Input the key
    key = "0123456789ABCDEF"  # input("Enter the key: ")
    if len(key) == 0:
        print("Key cannot be empty.")
        return

    # Read the sound file
    filename = "input.wav"
    params, sound_data = read_sound_file(filename)

    # Convert key and sound data to lists of integers
    key = [ord(char) for char in key]

    # Initialize S vector
    S_vector = list(range(0, 256))
    S_vector_mod = modify_S_vector(key, S_vector)

    # Encrypt the sound file
    encrypted_sound_data = encrypt(sound_data, S_vector_mod)

    # Write the encrypted sound file
    encrypted_filename = "encrypted.wav"
    write_sound_file(encrypted_filename, params, encrypted_sound_data)
    print("Encryption completed.")

    # Decrypt the encrypted sound file
    decrypted_sound_data = decrypt(encrypted_sound_data, S_vector_mod)

    # Write the decrypted sound file
    decrypted_filename = "decrypted.wav"
    write_sound_file(decrypted_filename, params, decrypted_sound_data)
    print("Decryption completed.")


if __name__ == "__main__":
    main()
