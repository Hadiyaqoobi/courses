#!/usr/bin/env python3

import unittest


from validations import validate_usr

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_usr("validuser", 3), True)
        
    def test_too_short(self):
        self.assertEqual(validate_usr("inv", 5), False)
        
    def test_invalid_characters(self):
        self.assertEqual(validate_usr("invalid_user", 1), False)
        
    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_usr, "user", -1)
        
        

#Run the tests
unittest.main()