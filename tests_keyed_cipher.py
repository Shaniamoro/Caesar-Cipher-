"""
    tests_keyed_cipher.py
    ---------------

    This module contains the unittests used to test the code from the Keyed_Caesar module.
    We are testing that the correct result is returned from each of the functions in the cipher.

"""
__author__ = "Shania Roberts"

import unittest

from keyed_caesar import KeyCaesar


class KeyedCaesarTest(unittest.TestCase):
    """
    This class contains the unittests used for testing the code.
    """

    def setUp(self) -> None:
        """
        Creates an instance of the class :class:`Keyed_Caesar.KeyCaesar` to be used in the tests.
        :return: Passing Test
        """
        self.test_class = KeyCaesar()

    def test_cipher_key_removes_duplicate_letters(self):
        """
        Checks if the correct key is returned from the cipher_key function.
        This means the duplicate characters were removed.

        :return: Passing Test
        """
        key = self.test_class.cipher_key("whatyouget")
        self.assertEqual(['w', 'h', 'a', 't', 'y', 'o', 'u', 'g', 'e'], key)

    def test_cipher_alphabet_is_accurate(self):
        """
        Checks if the correct alphabet is returned from the cipher_alphabet function.
        This means the key was applied correctly.

        :return: Passing Test
        """
        alpha = self.test_class.cipher_alphabet(['w', 'h', 'a', 't', 'y', 'o', 'u', 'g', 'e'])
        self.assertEqual({'a': 'w', 'b': 'h', 'c': 'a', 'd': 't', 'e': 'y', 'f': 'o', 'g': 'u', 'h': 'g', 'i': 'e',
                          'j': 'b', 'k': 'c', 'l': 'd', 'm': 'f', 'n': 'i', 'o': 'j', 'p': 'k', 'q': 'l', 'r': 'm',
                          's': 'n', 't': 'p', 'u': 'q', 'v': 'r', 'w': 's', 'x': 'v', 'y': 'x', 'z': 'z'}, alpha)

    def test_if_encoded_message_is_accurate(self):
        """
        Checks if the encoded message is as expected.

        :return: Passing test
        """
        message = self.test_class.encode_message(['w', 'h', 'a', 't', 'y', 'o', 'u', 'g', 'e'], 'the cat in the hat')
        self.assertEqual('pgy awp ei pgy gwp', message)

    def test_if_decoded_message_is_accurate(self):
        """
        Checks if the decoded message is as expected.

        :return: Passing Test
        """
        message = self.test_class.decode_message(['w', 'h', 'a', 't', 'y', 'o', 'u', 'g', 'e'], 'pgy awp ei pgy gwp')
        self.assertEqual('the cat in the hat', message)
