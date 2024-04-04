import unittest
from math import sqrt
class TestCalculator(unittest.TestCase):

  def word_counter(file):
    text = file
    lst_no = ['.', ',', ':', '!', '"', "'", '[', ']', '-', '—', '(', ')']
    lst = []

    for word in text.lower().split():
        if not word in lst_no:
            _word = word
            if word[-1] in lst_no:
                _word = _word[:-1]
            if word[0] in lst_no:
                _word = _word[1:]
            lst.append(_word)

    _dict = dict()
    for word in lst:
        _dict[word] = _dict.get(word, 0) + 1


    _list = []
    for key, value in _dict.items():
        _list.append((value, key))
        _list.sort(reverse=True)



    for freq, word in _list[0:10]:
        return word
  def test_one(self):
    self.assertEqual(TestCalculator.word_counter("gggg gg gggg gg gggg y y yy"), 'gggg')

  def test_two(self):
    self.assertEqual(TestCalculator.word_counter("gggg gg gggg gg gggg y y y y"), 'y')

  def test_three(self):
    self.assertEqual(TestCalculator.word_counter("gg gg gg gg gg gg gggg y y y y"), 'gg')
if __name__ == "__main__":
  unittest.main()