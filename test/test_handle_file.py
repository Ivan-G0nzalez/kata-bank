from src.handle_file import HandleFile
from assertpy import assert_that

import os
import pytest

def test_read_data():
    handle_file = HandleFile("test/test_write_file/data.txt", None)
    expected = "123456\n654321\n789012"
    got_data = handle_file.read_data()
    assert got_data == expected

def test_convert_data_str():
    handle_file = HandleFile(None, None)
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]]
    expected = ["123", "456", "7890"]
    assert_that(handle_file._convert_data_str(input_list)).is_equal_to(expected)
    assert_that(handle_file._convert_data_str(input_list)).contains("123")

def test_format_number():
    assert HandleFile.format_number([1, 2, 3]) == "1\n2\n3"

def test_ambiguous_number_format():
    assert HandleFile.ambiguous_number_format([1, 2, 3], [[1, 2, 3], [1, 2, 8]]) == ("123", ["123", "128"])