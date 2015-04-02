# Practical ![Build](https://travis-ci.org/cuhsat/practical.svg)
The Practical Cipher `0.1.0`

A one-time pad variant for easy manual application. Based on a 6x6 conversion
table supporting alphanumeric symbols. Random key generation can be done with
a normal gambling dice (d6).

An implementation in Python is provided.

## Usage
```$ practical.py COMMAND [KEY TEXT...]```

### Commands
* `-e` Encrypts the given text
* `-d` Decrypts the given text
* `-g` Generates a random key block
* `-h` Shows this text
* `-l` Shows the license
* `-v` Shows the version

## Usage as library
The Python modul exports the `Practical` class.

> Please note, that the used key must have the same length as the encrypted /
> decrypted text and must *never be used twice*.

### Practical.encrypt(text, key)
Returns the given `text` encrypted with the given `key` as a string.

### Practical.decrypt(text, key)
Returns the given `text` decrypted with the given `key` as a string.

### Practical.generate(size)
Returns a new random key block of the given `size` as a string.

### Example
```
from practical import Practical

practical = Practical()

plaintext, key = "Hello", practical.generate(5)

encrypted = practical.encrypt(plaintext, key)
decrypted = practical.decrypt(encrypted, key)
```

## Tests
```$ practical_test.py```

> For testing the _py.test_ modul is required.

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute
this software, either in source code form or as a compiled binary, for any
purpose, commercial or non-commercial, and by any means.

Christian Uhsat <christian@uhsat.de>
