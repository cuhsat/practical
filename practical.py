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
import os
import re
import random
import sys


__all__, __version__ = ["Practical"], "0.1.2"


class Practical(object):
    """
    The Practical Cipher.
    """
    def __init__(self, table=None):
        """
        Sets the used conversion table.
        """
        self.table = table or [
            ["A", "B", "C", "D", "E", "F"],
            ["G", "H", "I", "J", "K", "L"],
            ["M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X"],
            ["Y", "Z", "0", "1", "2", "3"],
            ["4", "5", "6", "7", "8", "9"]
        ]

    def __crypt(self, text, key, mode):
        """
        Returns the crypted text.
        """
        text = re.sub("[^A-Z0-9]", "", text.upper())
        key  = re.sub("[^A-Z0-9]", "", key.upper())

        if len(text) != len(key):
            raise Exception("Key length does not match")

        def lookup(symbol, table="".join([x for y in self.table for x in y])):
            return reversed(divmod(table.index(symbol), 6))

        output = ""

        for i in range(len(text)):
            tx, ty = lookup(text[i])
            kx, ky = lookup(key[i])

            rx = mode(tx, kx) % 6
            ry = mode(ty, ky) % 6

            output += self.table[ry][rx]

        return output

    def encrypt(self, text, key):
        """
        Returns the encrypted text.
        """
        return self.__crypt(text, key, lambda x, y: (x + y))

    def decrypt(self, text, key):
        """
        Returns the decrypted text.
        """
        return self.__crypt(text, key, lambda x, y: (x - y))

    def generate_block(self, size=5):
        """
        Returns a new random key block.
        """
        block, r = "", random.SystemRandom()

        for i in range(size):
            x = r.randint(0, 5)
            y = r.randint(0, 5)

            block += self.table[y][x]

        return block

    def generate_page(self, size=5, cols=5, rows=15):
        """
        Returns a new random key page.
        """
        page = ""

        for row in range(rows):
            for col in range(cols):
                page += self.generate_block(size) + " "
            else:
                page += "\n"

            if (row + 1) % 5 == 0:
                page += "\n"

        return page.rstrip()


def main(script, command="--help", key=None, *text):
    """
    Usage: %s COMMAND [KEY TEXT...]

    Commands:
      -b --generate-block   Generates a random key block
      -p --generate-page    Generates a random key page

      -d --decrypt   Decrypts the given text
      -e --encrypt   Encrypts the given text

      -h --help      Shows this text
      -l --license   Shows the license
      -v --version   Shows the version

    Report bugs to <christian@uhsat.de>
    """
    try:
        script = os.path.basename(script)

        if command in ("/?", "-h", "--help"):
            print(re.sub("(?m)^ {4}", "", main.__doc__ % script).strip())

        elif command in ("-l", "--license"):
            print(__doc__.strip())

        elif command in ("-v", "--version"):
            print("Practical Cipher " + __version__)

        elif command in ("-d", "--decrypt") and key and text:
            print(Practical().decrypt(" ".join(text), key))

        elif command in ("-e", "--encrypt") and key and text:
            print(Practical().encrypt(" ".join(text), key))

        elif command in ("-b", "--generate-block"):
            print(Practical().generate_block())

        elif command in ("-p", "--generate-page"):
            print(Practical().generate_page())

        else:
            print("Unknown command or parameter not given.")
            print("Please use --help for help on commands.")
            return 2 # Incorrect usage

    except Exception as ex:
        return "%s error: %s" % (script, ex)


if __name__ == "__main__":
    sys.exit(main(*sys.argv))
