import unittest

from sample import main


class Tests(unittest.TestCase):
    def prepare(self, line):
        strCards = line.replace('\n', '').split(' ')
        cards = []
        for i, strCard in enumerate(strCards):
            cards.append(main.strToCard(strCard, i))
        return cards

    def test_strToCard(self):
        self.assertEqual(main.strToCard("2D", 1), {'suit': 'D', 'face': 2, 'position': 1})
        self.assertEqual(main.strToCard("KS", 7), {'suit': 'S', 'face': 13, 'position': 7})
        self.assertEqual(main.strToCard("QH", 5), {'suit': 'H', 'face': 12, 'position': 5})
        self.assertEqual(main.strToCard("TH", 0), {'suit': 'H', 'face': 10, 'position': 0})
        self.assertEqual(main.strToCard("QH", 5), {'suit': 'H', 'face': 12, 'position': 5})

    def test_straight(self):
        cards = self.prepare("AC 2D 9C 3S KD 5S 4D KS AS 4C")
        self.assertTrue(main.straight(cards))
        cards = self.prepare("6C 9C 8C 2D 7C 2H TC 4C 9S AH")
        self.assertFalse(main.straight(cards))

    def test_n_of_a_kind(self):
        cards = self.prepare("2H 2S 3H 3S 3C 2D 3D 6C 9C TH")
        self.assertTrue(main.n_of_a_kind(4, cards))
        cards = self.prepare("AH 2C 9S AD 3C QH KS JS JD KD")
        self.assertFalse(main.n_of_a_kind(3, cards))

    def test_n_m_of_a_kind(self):
        cards = self.prepare("2H 2S 3H 3S 3C 2D 9C 3D 6C TH")
        self.assertTrue(main.n_m_of_a_kind(2, 3, cards))
        cards = self.prepare("KS AH 2H 3C 4H KC 2C TC 2D AS")
        self.assertFalse(main.n_m_of_a_kind(2, 3, cards))

    def test_flush(self):
        cards = self.prepare("2H AD 5H AC 7H AH 6H 9H 4H 3C")
        self.assertTrue(main.flush(cards))
        cards = self.prepare("AC 2D 9C 3S KD 5S 4D KS AS 4C")
        self.assertFalse(main.flush(cards))

    def test_straight_flush(self):
        cards = self.prepare("TH JH QC QD QS QH KH AH 2S 6S")
        self.assertTrue(main.straight_flush(cards))
        cards = self.prepare("6C 9C 8C 2D 7C 2H TC 4C 9S AH")
        self.assertFalse(main.straight_flush(cards))

    def test_fit(self):
        comb = [0,1,2,5,6]
        self.assertTrue(main.fit(comb))
        comb = [0, 1, 2, 3, 8]
        self.assertFalse(main.fit(comb))


if __name__ == '__main__':
    unittest.main()