# Vigenère Cipher Implementation

This project implements the Vigenère cipher for encrypting and decrypting messages using a custom key.

## Overview

The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. It uses a keyword to determine the shift applied to each character in the plaintext.

## Features

- Encryption of messages using a custom key.
- Decryption of encrypted messages using the same key.
- Support for handling non-alphabetic characters gracefully.

## Getting Started

#### **Prerequisites** 
- Python 3.x
#### **Installation**
No installation is required. Simply download or clone the repository to your local machine.

## Usage

1. Import the Vigenère cipher module into your Python project.

        from vigenere_cipher import encrypt, decrypt

2. Encrypt a message using a custom key:

        text = 'mrttaqrhknsw ih puggrur'
        custom_key = 'happycoding'
        encrypted_message = encrypt(text, custom_key)
        print(f'Encrypted message: {encrypted_message}')

3. Decrypt an encrypted message using the same key:

        decrypted_message = decrypt(encrypted_message, custom_key)
        print(f'Decrypted message: {decrypted_message}')

## Example

        from vigenere_cipher import encrypt, decrypt

        text = 'mrttaqrhknsw ih puggrur'
        custom_key = 'happycoding'

        encrypted_message = encrypt(text, custom_key)
        print(f'Encrypted message: {encrypted_message}')

        decrypted_message = decrypt(encrypted_message, custom_key)
        print(f'Decrypted message: {decrypted_message}')

## Credits

This project is part of my coursework for Freecodecamp and contributes to my certificate project.