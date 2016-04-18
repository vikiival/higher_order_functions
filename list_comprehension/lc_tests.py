import lc_exercises as lc
import unittest

class ListTests(unittest.TestCase):
    def test_first(self):
        self.assertEqual(lc.first([1,2,4,5,6]), 1)


    def test_last(self):
        self.assertEqual(lc.last([1,2,4,5,6]), 6)


    def test_interval(self):
        self.assertEqual(lc.interval([1,2,4,5,6], 1,3), [2,4,5])


    def test_no_first_two(self):
        self.assertEqual(lc.no_first_two([1,2,4,5,6]), [4,5,6])


    def test_no_last_three(self):
        self.assertEqual(lc.no_last_three([1,2,4,5,6]), [1,2])


    def test_every_second(self):
        self.assertEqual(lc.every_second([1,2,4,5,6]), [1,4,6])


    # List comprehension
    def test_square(self):
        self.assertEqual(lc.square([1,2,3,4,5,6]), [1,4,9,16,25,36])


    def test_plus_one(self):
        self.assertEqual(lc.plus_one([1,2,3,4,5,6]), [2,3,4,5,6,7])


    def test_evens(self):
        self.assertEqual(lc.evens([1,2,3,4,5,6]), [2,4,6])


    def test_multiples(self):
        self.assertEqual(lc.multiples(50), [3, 9, 15, 21, 27, 33, 39, 45])


    def test_first_chars(self):
        self.assertEqual(lc.first_chars("On second thought, let's not go to Camelot. It is a silly place."),
                         ['O', 's', 't', 'l', 'n', 'g', 't', 'C', 'I', 'i', 'a', 's', 'p'])


    def test_unique_consonants(self):
        self.assertEqual(lc.unique_consonants("On second thought, let's not go to Camelot. It is a silly place."),
                         {'c', 'd', 'g', 'h', 'l', 'm', 'n', 'p', 's', 't'})


    def test_replace_vowels(self):
        self.assertEqual(lc.replace_vowels("On second thought, let's not go to Camelot. It is a silly place."),
                         "0n s0c0nd th00ght, l0t's n0t g0 t0 C0m0l0t. 0t 0s 0 s0ll0 pl0c0.")


    def test_word_combinations(self):
        words1 = ['Lancelot', 'Robin', 'Galahad']
        words2 = ['Camelot', 'Assyria']

        self.assertEqual(lc.word_combinations(words1, words2),
                         [('Lancelot', 'Camelot'), ('Lancelot', 'Assyria'), ('Robin', 'Camelot'),
                          ('Robin', 'Assyria'), ('Galahad', 'Camelot'), ('Galahad', 'Assyria')])


    def test_two_dices(self):
        self.assertEqual(lc.two_dices(), [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)])


    def test_array(self):
        self.assertEqual(lc.array(2, 3), [[None, None, None], [None, None, None]])
        self.assertEqual(lc.array(3, 3, 0), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])


    def test_combinations_of_two(self):
        self.assertEqual(lc.combinations_of_two([1,2,3]), [[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])



    def test_combinations_of_two_no_rep(self):
        self.assertEqual(lc.combinations_of_two_no_rep([1,2,3]), [[1,2], [1,3], [2,1], [2,3], [3,1], [3,2]])


    def test_pytagoreans(self):
        self.assertEqual(lc.pytagoreans(25), [[3, 4, 5], [5, 12, 13], [6, 8, 10], [8, 15, 17], [9, 12, 15], [12, 16, 20]])


if __name__ == '__main__':
    unittest.main()
