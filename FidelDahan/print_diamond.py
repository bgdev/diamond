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
    letters = [Letter(x) for x in Letter.ALPHABET]
    self.spans = [Span(x) for x in letters
                  if x.index < self.equator.letter.index]

  def render(self):
    lines_above = [self.indent(x) + x.render() for x in self.spans]
    lines_below = [self.indent(x) + x.render() for x in reversed(self.spans)]
    middle_line = [self.equator.render()]
    return "\n".join(lines_above + middle_line + lines_below)

  def indent(self, span:Span):
    distance = self.equator.letter.index - span.letter.index
    return " " * distance


def args():
  parser = ArgumentParser(description="Prints a diamond with the letters A..Z")
  parser.add_argument("letter", choices=[x for x in Letter.ALPHABET])
  return parser.parse_args()


if __name__ == '__main__':
  print(Diamond(args().letter).render())