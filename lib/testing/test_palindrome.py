# lib/testing/test_palindrome.py

import pytest
from lib.palindrome import longest_palindromic_substring

# ----- NORMAL CASES -----
def test_babad():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_cbbd():
    assert longest_palindromic_substring("cbbd") == "bb"

# ----- EDGE CASES -----
def test_single_character():
    assert longest_palindromic_substring("a") == "a"

def test_two_characters():
    assert longest_palindromic_substring("ac") in ["a", "c"]

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"

def test_full_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

# ----- SPECIAL CASES -----
def test_no_long_palindrome():
    result = longest_palindromic_substring("abc")
    assert result in ["a", "b", "c"]

def test_long_palindrome_middle():
    assert longest_palindromic_substring("xabax") == "xabax"

def test_palindrome_at_end():
    assert longest_palindromic_substring("xyzzy") == "yzzy"