#!/bin/bash env python3

import unittest
import skrypt

class Test(unittest.TestCase):
    def test_word(self):
        self.assertEqual(skrypt.wypisz_wyraz('królików'), 'królików')

    def test_number(self):
        self.assertEqual(skrypt.wypisz_liczbe('70'), '70')


if __name__ == '__main__':
    unittest.main()
