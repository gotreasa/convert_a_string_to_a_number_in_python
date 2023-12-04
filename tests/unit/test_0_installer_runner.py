import os

from modules import number_from_string


def describe_dummy_kata():
    def should_print_title(capsys):
        """🧪 expect the dummy kata prints the title"""
        number_from_string.print_the_title()
        out, _err = capsys.readouterr()
        assert "😊 Welcome to Dummy Kata" in out
