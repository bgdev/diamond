from unittest import TestCase


class Letter(object):
  ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def __init__(self, char):
    self.char = char
    self.index = self.ALPHABET.index(char)


class LetterTest(TestCase):

  def test_index_of_first_letters(self):
    self.assertEquals(0, Letter('A').index)
    self.assertEquals(1, Letter('B').index)
    self.assertEquals(2, Letter('C').index)

  def test_index_of_last_letters(self):
    self.assertEquals(23, Letter('X').index)
    self.assertEquals(24, Letter('Y').index)
    self.assertEquals(25, Letter('Z').index)


class Span(object):
  def __init__(self, letter:Letter):
    self.letter = letter

  def render(self):
    if self.letter.char == 'A':
      return "{}".format(self.letter.char)
    else:
      space_count = 2 * self.letter.index - 1
      return "{}{}{}".format(self.letter.char,
                             " " * space_count,
                             self.letter.char)


class SpanTest(TestCase):
  def test_render_first_letters(self):
    self.assertEquals("A", Span(Letter('A')).render())
    self.assertEquals("B B", Span(Letter('B')).render())
    self.assertEquals("C   C", Span(Letter('C')).render())

  def test_render_last_letters(self):
    self.assertEquals("X                                             X",
                      Span(Letter('X')).render())
    self.assertEquals("Y                                               Y",
                      Span(Letter('Y')).render())
    self.assertEquals("Z                                                 Z",
                      Span(Letter('Z')).render())

# TODO
