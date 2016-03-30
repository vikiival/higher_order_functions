import hof_exercises as hof
import unittest

class HofTests(unittest.TestCase):
    def test_square(self):
        self.assertEqual(hof.square([1,2,3,4,5]), [1,4,9,16,25])

    def test_even(self):
        self.assertEqual(hof.even([1,2,3,4,5]), [2, 4])


    def test_to_fahrenheit(self):
        self.assertEqual(hof.to_fahrenheit((36.5, 37, 37.5, 38, 39)), [97.7, 98.60000000000001, 99.5, 100.4, 102.2])

    def test_arthur_speaking(self):
        self.assertEqual(hof.arthur_speaking('../data/holy_grail.txt')[:2],[
                             "  ARTHUR:  Whoa there!\n",
                             "  ARTHUR:  It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.  King of the Britons, defeator of the Saxons, sovereign of all England!\n"
                          ])

    def test_arthur_speaking_clear(self):
        self.assertEqual(hof.arthur_speaking_clear('../data/holy_grail.txt')[:2],[
                             "Whoa there!",
                             "It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.  King of the Britons, defeator of the Saxons, sovereign of all England!"
                          ])


    def test_line_count(self):
        self.assertEqual(hof.line_count('../data/holy_grail.txt'), 44)



    def test_word_count(self):
        self.assertEqual(hof.word_count('../data/holy_grail.txt'), [2, 1, 2, 3, 2, 6, 26, 6, 40, 7, 2, 5, 2, 13, 19, 7, 4, 9, 5, 8, 30, 7, 8, 9, 8, 29, 21, 21, 2, 5, 4, 10, 16, 8, 15, 11, 4, 10, 2, 12, 11, 10, 9, 5])



    def test_total_words(self):
        self.assertEqual(hof.total_words('../data/holy_grail.txt'), 436)


    def test_my_max(self):
        self.assertEqual(hof.my_max([12,3,5,7,11,111,-555]), 111)



    def test_my_mean(self):
        self.assertEqual(hof.my_mean(range(101)), 50)



    def test_my_std(self):
        self.assertEqual(hof.my_std([2,4,4,4,5,5,7,9]), 2.0)

    def test_flatten(self):
        self.assertEqual(hof.flatten([[1,2,3],[4],[5,6],[7]]), [1,2,3,4,5,6,7])

    def test_histogram(self):
        self.assertEqual(sorted(hof.histogram('../data/holy_grail.txt').most_common(9), key=lambda x: x[0]),
                         [('1', 20), ('a', 14), ('arthur', 17), ('guard', 24), ('it', 10), ('not', 8), ('of', 15), ('the', 17), ('you', 8)])


if __name__ == '__main__':
    unittest.main()