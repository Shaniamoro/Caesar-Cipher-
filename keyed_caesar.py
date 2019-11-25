"""
    keyed_caesar.py
    ---------------

    This contains an implementation of a Keyed Caesar cipher.

"""
__author__ = "Shania Roberts"

import string


class KeyCaesar:
    """
    The KeyCaesar class implements the cipher.
    """

    def __init__(self):
        pass

    @staticmethod
    def cipher_key(input_key):
        """
        Converts user input into the cipher key.
        Removes duplicate letters.

        :param input_key: String of the cipher key.
        :return key: A list which is the cipher key
        """
        key = []
        for letter in input_key:
            if letter not in key:
                key.append(letter)
        return key

    @staticmethod
    def cipher_alphabet(key):
        """
        Creates an alphabet to encode/decode user input.

        :param key: The key returned from the method cipher_key().
        :return new_alpha: A list which is used to encode the message.
        """
        new_alpha = {}
        letters = list(string.ascii_lowercase)
        temp_list = [x for x in letters if x not in key]
        length_of_key = len(key)

        for i in range(length_of_key):
            new_alpha[letters[i]] = key[i]
        j = 0
        for i in range(length_of_key, len(letters)):
            new_alpha[letters[i]] = temp_list[j]
            j += 1
        return new_alpha

    def encode_message(self, key, user_input):
        """
        Encodes the message given by the user.
        Uses the new alphabet created by the key to create a secret message.

        :param key: The key returned from the method cipher_key().
        :param user_input: A string of the message to be encoded.
        :return new_string: A string containing the encoded message.
        """
        encoding = self.cipher_alphabet(key)
        new_string = ''
        for letter in user_input:
            if letter == ' ':
                new_string += letter
            else:
                new_string += encoding[letter]
        return new_string

    def decode_message(self, key, user_input):
        """
        Decodes the message given by the user.
        Uses the new alphabet created by the key to create a secret message.

        :param key: The key returned from the method cipher_key().
        :param user_input: A string of the message to be decoded.
        :return new_string: A string containing the decoded message.
        """
        temp = self.cipher_alphabet(key)
        encoding = {value: key for key, value in temp.items()}
        new_string = ''
        for letter in user_input:
            if letter == ' ':
                new_string += letter
            else:
                new_string += encoding[letter]
        return new_string

    def run_cipher(self, user_key, user_message, user_val):
        """
        Acts as the driver of the program.
        Accepts user input and either encodes or decodes a message.
        Calls upon the following methods:
         :func:`keyed_caesar.KeyCaesar.cipher_key`
         :func:`keyed_caesar.KeyCaesar.encode_message`
         :func:`keyed_caesar.KeyCaesar.decode_message`

        :return message: A string of the encoded or decoded message.
        """
        decision = user_val.upper()
        key = user_key.lower()
        user_input = user_message.lower()
        if decision == 'E':
            message = self.encode_message(key, user_input)
        elif decision == 'D':
            message = self.decode_message(key, user_input)
        else:
            print("Incorrect entry: please enter 'E' or 'D' ")
            self.run_cipher()
        return message
