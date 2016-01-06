from argparse import ArgumentParser
import os
from unittest import TestCase
import sys
from print_diamond import *


class LetterTest(TestCase):

  def test_index_of_first_letters(self):
    self.assertEquals(0, Letter('A').index)
    self.assertEquals(1, Letter('B').index)
    self.assertEquals(2, Letter('C').index)

  def test_index_of_last_letters(self):
    self.assertEquals(23, Letter('X').index)
    self.assertEquals(24, Letter('Y').index)
    self.assertEquals(25, Letter('Z').index)

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


class DiamondTest(TestCase):
  def test_render_A(self):
    self.assertEqual("A", Diamond('A').render())

  def test_render_B(self):
    self.assertEqual(" A\nB B\n A", Diamond('B').render())

  def test_render_C(self):
    self.assertEqual("  A\n B B\nC   C\n B B\n  A", Diamond('C').render())


class EndToEndTest(TestCase):
  def test(self):
    os.exec