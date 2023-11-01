import pytest

from main import encryptThis


def test_encryptThis_five_letters():
  assert encryptThis("Hello") == '72olle'

def test_encryptThis_four_letters():
  assert encryptThis("good") == '103doo'

def test_encryptThis_two_words():
  assert encryptThis("hello world") == '104olle 119drlo'

def test_encryptThis_empty_message():
  assert encryptThis("") == ''
