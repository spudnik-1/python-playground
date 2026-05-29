import unittest
from unittest.mock import patch
import sys
from io import StringIO

import complete_me

class CompleteMeTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(complete_me.greet("Pickle"), "Hello, Pickle! You are amazing :)")
    
    def test_how_hot_is_it(self):
        self.assertEqual(complete_me.how_hot_is_it(0), "ICE ICE BABY")
        self.assertEqual(complete_me.how_hot_is_it(10), "Bring me a blanket")
        self.assertEqual(complete_me.how_hot_is_it(22), "Nice and cozy")
        self.assertEqual(complete_me.how_hot_is_it(30), "FEELIN' HOT HOT HOT")    

    def test_print_all_numbers_between_one_and_twenty_divisible_by_three(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            complete_me.print_all_numbers_between_one_and_twenty_divisible_by_three()
            self.assertEqual(fake_out.getvalue(), "3\n6\n9\n12\n15\n18\n")

    def test_do_you_need_a_cookie(self):
        with patch('builtins.input', return_value="Yes"):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                complete_me.do_you_need_a_cookie()
                self.assertEqual(fake_out.getvalue(), "Do you need a cookie?\nGo have a cookie. You deserve it :)\n")
    
    def test_find_num_bikes(self):
        self.assertEqual(complete_me.find_num_bikes(), 332)

if __name__ == "__main__":
    unittest.main()
