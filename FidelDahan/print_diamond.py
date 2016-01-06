#!/usr/bin/env python3
from argparse import ArgumentParser


class Letter(object):
  ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def __init__(self, char):
    self.char = char
    self.index = self.ALPHABET.index(char)


class Span(object):
  def __init__(self, letter:Letter):
    self.letter = letter

  def render(self):
    if self.letter.char == 'A':
      return "A"
    else:
      space_count = 2 * self.letter.index - 1
      return "{}{}{}".format(self.letter.char,
                             " " * space_count,
                             self.letter.char)


class Diamond(object):
  def __init__(self, of:str):
    self.equator = Span(Letter(of))
    self.spans = [Span(letter)
                  for letter in [Letter(char) for char in Letter.ALPHABET]
                  if letter.index < self.equator.letter.index]

  def render(self):
    lines_above = [self.indent(span) + span.render() for span in self.spans]
    lines_below = [self.indent(span) + span.render() for span in reversed(self.spans)]
    middle_line = [self.equator.render()]
    return "\n".join(lines_above + middle_line + lines_below)

  def indent(self, span:Span):
    space_count = self.equator.letter.index - span.letter.index
    return " " * space_count


def args():
  parser = ArgumentParser(description="Prints a diamond with the letters A..Z")
  parser.add_argument("char", choices=[char for char in Letter.ALPHABET])
  return parser.parse_args()


if __name__ == '__main__':
  print(Diamond(args().char).render())