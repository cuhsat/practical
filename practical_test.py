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
    sys.exit("Requires py.test (https://pytest.org)")


class TestPractical:
    """
    The Practical Cipher unit tests.
    """
    vectors = [("HELLOWORLD", "XUJW7W6OKJ", "QWERTASDFG")]

    def test_encrypt(self):
        """
        Encryption test.
        """
        for source, expect, key in self.vectors:
            assert expect == Practical(True).encrypt(source, key)

    def test_decrypt(self):
        """
        Decryption test.
        """
        for expect, source, key in self.vectors:
            assert expect == Practical(True).decrypt(source, key)

    def test_generate(self):
        """
        Key generation test.
        """
        assert re.match("^[A-Z0-9]{32}$", Practical().generate(32))


if __name__ == "__main__":
    sys.exit(pytest.main(list(sys.argv)))
