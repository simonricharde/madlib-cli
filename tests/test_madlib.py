import madlib_cli.madlib
import pytest

def test_read_file_exists():
   assert madlib_cli.madlib.read_file

def test_read_file_does_not_exists():
   with pytest.raises(FileNotFoundError):
       madlib_cli.madlib.read_file("assets/spam.txt")

def test_get_templates():
    file_contents = 'It was a {Adjective} and {Adjective} {Noun}'
    expected = ['Adjective', 'Adjective', 'Noun']
    assert madlib_cli.madlib.get_templates(file_contents) == expected


def test_remove_templates():
    file_contents = 'It was a {Adjective} and {Adjective} {Noun}'
    expected = 'It was a {} and {} {}'
    assert madlib_cli.madlib.remove_templates(file_contents) == expected


def test_write_file():
    madlib_cli.madlib.write_file('./test.txt', 'test')
    with open('./test.txt') as file:
        assert file.read() == 'test'
