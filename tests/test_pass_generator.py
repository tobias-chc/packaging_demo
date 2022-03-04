# Tests (copy to tests/test_user_functions.py)
import pytest
import os
import io

from src.user_functions import *

# Password Length tests

# GPLI = get_password_length_input

def test_GPLI_not_integer(monkeypatch):
    # Set the console input to: Six
    monkeypatch.setattr('sys.stdin', io.StringIO('Six'))
    assert get_password_length_input() is None

def test_GPLI_smaller_minLength(monkeypatch):
    # Set the console input to: 5
    monkeypatch.setattr('sys.stdin', io.StringIO('5'))
    assert get_password_length_input() is None

def test_GPLI_larger_maxLength(monkeypatch):
    # Set the console input to: 16
    monkeypatch.setattr('sys.stdin', io.StringIO('16'))
    assert get_password_length_input() is None

def test_GPLI_correct(monkeypatch):
    # Set the console input to: 16
    monkeypatch.setattr('sys.stdin', io.StringIO('12'))
    assert get_password_length_input() is 12
