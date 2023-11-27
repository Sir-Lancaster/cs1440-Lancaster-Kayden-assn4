#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.


import unittest


# A demonstration of how to use the assertions provided by the unittest library.
#
# These are all TRIVIAL tests that DO NOT count towards the required number
# of tests.


def returnsNone():
    "This is a function that returns None"

def returnsSomething():
    return "This is a function that returns something besides None"


def unsafe_convert(obj, new_type):
    """
    Convert 'obj' to 'new_type' with crashing

    :param obj: An object to convert into a new type
    :param new_type: Type constructor function

    :return: A new object of type 'new_type', or raise ValueError
    """
    if not type(new_type) == type:
        raise ValueError(f"Second argument must be a valid Python type")
    return new_type(obj)


def safe_convert(obj, new_type):
    """
    Convert 'obj' to 'new_type' without crashing.

    :param obj: An object to convert into a new type
    :param new_type: Type constructor function

    :return: A new object of type 'new_type', or None if the conversion is not possible
    """
    if not type(new_type) == type:
        raise ValueError(f"Second argument must be a valid Python type")
    try:
        return new_type(obj)
    except ValueError:
        return None



class TestAssertions(unittest.TestCase):

    def test_True(self):
        a = True
        self.assertTrue(a)

        # Certain Python values can be converted to Boolean true:
        a = 1
        self.assertTrue(a)
        a = -1
        self.assertTrue(a)
        a = "true"
        self.assertTrue(a)
        a = {'this dictionary': 'is not empty'}
        self.assertTrue(a)


    def test_False(self):
        a = False
        self.assertFalse(a)

        # As above, certain Python values can be converted to Boolean false:
        a = 0
        self.assertFalse(a)
        a = ""
        self.assertFalse(a)
        a = {}
        self.assertFalse(a)


    def test_Equal(self):
        a = 'A string'
        b = 'A string'
        self.assertEqual(a, b)

        a = 1
        b = 1
        self.assertEqual(a, b)

        # In Python floating-point numbers are indistinguishable after 17
        # decimal places
        a = 1.00000000000000001
        b = 1.00000000000000002
        self.assertEqual(a, b)


    def test_NotEqual(self):
        a = 'A string'
        b = 'Another string'
        self.assertNotEqual(a, b)

        a = 1
        b = 2
        self.assertNotEqual(a, b)

        # In Python these floating-point numbers differ in the 16th decimal
        # place, and are distinct
        a = 1.0000000000000001
        b = 1.0000000000000002
        self.assertNotEqual(a, b)


    def test_AlmostEqual(self):
        a = 3.141592653589793
        b = 102928 / 32763
        self.assertAlmostEqual(a, b)


    def test_Greater(self):
        a = 3.141592653589793
        b = 223/71
        self.assertGreater(a, b)


    def test_Less(self):
        a = 3.141592653589793
        b = 22/7
        self.assertLess(a, b)


    def test_Is(self):
        # The lists a & b have the same contents, and are, in fact, the same exact lists
        a = list(range(30))
        b = a
        self.assertEqual(a, b)
        self.assertIs(a, b)

        # Short strings are "interned"; even though these are different
        # variables, they both refer to the same piece of memory
        a = "Hello"
        b = "Hello"
        self.assertIs(a, b)


    def test_IsNot(self):
        # The lists a & b have the same contents, but are not actually the same exact lists
        a = list(range(30))
        b = list(range(30))
        self.assertEqual(a, b)
        self.assertIsNot(a, b)

        # Because these strings were not created in the same way, they are stored in different locations even though they are otherwise identical
        # identical, they are stored in different location.
        a = "Est ipsum ut labore dolore ipsum. Quaerat sit modi quisquam tempora. Adipisci modi porro tempora quaerat sit non adipisci. Aliquam quisquam sit dolore velit quaerat eius voluptatem. Dolor labore modi non eius aliquam. Aliquam modi quiquia magnam voluptatem sit. Quaerat modi numquam sit."
        b = ' '.join(["Est", "ipsum", "ut", "labore", "dolore", "ipsum.", "Quaerat", "sit", "modi", "quisquam", "tempora.", "Adipisci", "modi", "porro", "tempora", "quaerat", "sit", "non", "adipisci.", "Aliquam", "quisquam", "sit", "dolore", "velit", "quaerat", "eius", "voluptatem.", "Dolor", "labore", "modi", "non", "eius", "aliquam.", "Aliquam", "modi", "quiquia", "magnam", "voluptatem", "sit.", "Quaerat", "modi", "numquam", "sit.",])
        self.assertEqual(a, b)
        self.assertIsNot(a, b)


    def test_IsNone(self):
        a = None
        self.assertIsNone(a)
        self.assertIsNone(returnsNone())


    def test_IsNotNone(self):
        a = False
        self.assertIsNotNone(a)
        self.assertIsNotNone(returnsSomething())


    def test_In(self):
        needle = 'needle'
        haystack = [ "planetesimal", "cleared", "realizations", needle,
                "ballad", "pessimist", ]
        self.assertIn(needle, haystack)


    def test_NotIn(self):
        needle = 'needle'
        haystack = [ "planetesimal", "cleared", "realizations",
                "ballad", "pessimist", ]
        self.assertNotIn(needle, haystack)


    def test_CountEqual(self):
        a = list(range(30))
        b = tuple(range(30))
        self.assertCountEqual(a, b)


    def test_Raises(self):
        self.assertEqual(3.0, unsafe_convert("3", float))
        self.assertEqual(3, unsafe_convert("3", int))
        self.assertRaises(ValueError, unsafe_convert, None, len)
        self.assertRaises(ValueError, unsafe_convert, None, abs)
        self.assertRaises(ValueError, unsafe_convert, "3.0", int)
        self.assertRaises(ValueError, unsafe_convert, "three", float)

        self.assertEqual(3.0, safe_convert("3.0", float))
        self.assertEqual(3, safe_convert("3", int))
        self.assertRaises(ValueError, safe_convert, None, len)
        self.assertRaises(ValueError, safe_convert, None, abs)
        self.assertIsNone(safe_convert("3.0", int))
        self.assertIsNone(safe_convert("three", int))

        nums = list(range(20))
        self.assertEqual(20, len(nums))
        self.assertEqual(19, nums[19])
        # This doesn't do what you think it should
        # self.assertRaises(IndexError, nums[200])

        # Instead, you must write it like this (a rare instance where you
        # *need* to use a dunder's name):
        self.assertRaises(IndexError, nums.__getitem__, 200)


if __name__ == '__main__':
    unittest.main()
