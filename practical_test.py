#!/usr/bin/env python
"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
"""
import re
import sys


from practical import Practical


try:
    import pytest
except ImportError:
    sys.exit("Requires pytest (https://pytest.org)")


class TestPractical:
    """
    The Practical Cipher unit tests.
    """
    vectors = [
        ("AAAAAA", "999999", "999999"),
        ("999999", "999999", "AAAAAA"),
        ("A9A9A9", "A9A9A9", "AAAAAA"),
        ("9A9A9A", "9A9A9A", "AAAAAA"),
        ("A9A9A9", "999999", "9A9A9A"),
        ("ABCDEF", "AHOV29", "AGMSY4"),
        ("GHIJKL", "HOV29A", "BHNTZ5"),
        ("MNOPQR", "OV29AH", "CIOU06"),
        ("STUVWX", "V29AHO", "DJPV17"),
        ("YZ0123", "29AHOV", "EKQW28"),
        ("456789", "9AHOV2", "FLRX39"),
        ("AHOV29", "FR3FR3", "FKPUZ4"),
        ("ABCDEF", "468468", "456789"),
        ("456789", "468468", "ABCDEF"),
        ("HELLOX", "YV225E", "XXXXXX")
    ]

    def test_encrypt(self):
        """
        Encryption test.
        """
        for source, expect, key in self.vectors:
            assert Practical().encrypt(source, key) == expect

    def test_decrypt(self):
        """
        Decryption test.
        """
        for expect, source, key in self.vectors:
            assert Practical().decrypt(source, key) == expect

    def test_generate_block(self):
        """
        Key block generation test.
        """
        assert re.match("^[A-Z0-9]+$", Practical().generate_block())

    def test_generate_page(self):
        """
        Key page generation test.
        """
        assert re.match("^([A-Z0-9]|\s)+$", Practical().generate_page())


if __name__ == "__main__":
    sys.exit(pytest.main(list(sys.argv)))
