from RC4 import RC4
from utilites import *


def main():
    # Read the key
    key = input("Enter the key: ")
    if len(key) != 16:
        return print("Key must be 16 characters long.")

    # Read the sound file
    filename = "input.wav"
    params, sound_data = read_sound_file(filename)

    rc4 = RC4(key)

    # Encrypt the sound file
    encrypted_sound_data = rc4.encrypt(sound_data)

    # Write the encrypted sound file
    encrypted_filename = "encrypted.wav"
    write_sound_file(encrypted_filename, params, encrypted_sound_data)
    print("Encryption completed.")

    # Decrypt the encrypted sound file
    decrypted_sound_data = rc4.decrypt(encrypted_sound_data)

    # Write the decrypted sound file
    decrypted_filename = "decrypted.wav"
    write_sound_file(decrypted_filename, params, decrypted_sound_data)
    print("Decryption completed.")


if __name__ == "__main__":
    main()
