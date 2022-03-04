import pytest
import os
import io

from src.password_package import pass_generator as pg

# Password Length tests

# GPLI = get_password_length_input

def test_GPLI_not_integer(monkeypatch):
    # Set the console input to: Six
    monkeypatch.setattr('sys.stdin', io.StringIO('Six'))
    assert pg.get_password_length_input() is None


def test_GPLI_smaller_minLength(monkeypatch):
    # Set the console input to: 5
    monkeypatch.setattr('sys.stdin', io.StringIO('5'))
    assert pg.get_password_length_input() is None


def test_GPLI_larger_maxLength(monkeypatch):
    # Set the console input to: 16
    monkeypatch.setattr('sys.stdin', io.StringIO('16'))
    assert pg.get_password_length_input() is None


def test_GPLI_correct(monkeypatch):
    # Set the console input to: 16
    monkeypatch.setattr('sys.stdin', io.StringIO('12'))
    assert pg.get_password_length_input() is 12
