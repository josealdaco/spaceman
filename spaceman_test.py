import unittest
import six

from origin_spaceman import *
leftovers = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
values = [3, 7]
fill = []
class GreetByNameTests(unittest.TestCase):
    def test_greet(self):
        assert isinstance(load_word(), six.string_types) # This will check if you get a string


        self.assertEqual(character_display(7,7), """
                O
                |
              \ | /
                |
               / /
               """)
        self.assertEqual(character_display(6,7), """
                        O
                        |
                      \ | /
                        |
                       /
                        """)
        self.assertEqual(character_display(5,7), """
                        O
                        |
                      \ | /
                        |

                        """)
        self.assertEqual(character_display(4,7),  """
                        O
                        |
                      \ |
                        |

                        """)



        self.assertEqual(is_word_guessed("max", values), "Still in game")
        self.assertEqual(is_word_guessed("Table", values), "Still in game")
        self.assertEqual(is_word_guessed("Napkkn", values), "Still in game")
        self.assertEqual(is_word_guessed("lol", values), "Still in game")



        self.assertEqual(get_guessed_word("max", leftovers, values, fill), "Guess word so far: \nThese letters haven't been used though:asdfghjklzxcvbnmqwertyuiop\n You have a total of 7 incorrect guesses. ")
        self.assertEqual(get_guessed_word("Nani", leftovers, values, fill), "Guess word so far: \nThese letters haven't been used though:asdfghjklzxcvbnmqwertyuiop\n You have a total of 7 incorrect guesses. ")
        self.assertEqual(get_guessed_word("nevermind", leftovers, values, fill), "Guess word so far: \nThese letters haven't been used though:asdfghjklzxcvbnmqwertyuiop\n You have a total of 7 incorrect guesses. ")
        self.assertEqual(get_guessed_word("nothingchanges", leftovers, values, fill), "Guess word so far: \nThese letters haven't been used though:asdfghjklzxcvbnmqwertyuiop\n You have a total of 7 incorrect guesses. ")


if __name__ == "__main__":
    unittest.main()
print("Hello new file")
