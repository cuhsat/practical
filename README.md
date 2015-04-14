# Practical ![Build](https://travis-ci.org/cuhsat/practical.svg)
The Practical Cipher `0.1.1`

A one-time pad variant for easy manual application. Based on a 6x6 conversion
table supporting alphanumeric symbols. Random key generation can be done with
one normal gambling dice (d6).

An implementation in [Python](https://www.python.org) is provided.

## Specification

### Conversion Table
The conversion table uses a 6x6 alphanumeric matrix. It is filled from left
to right and from top to bottom with the uppercase letters of the alphabet
from `A` to `Z` and than the numbers from `0` to `9`.

The conversion table with the default symbol arrangement:
```
  | 0 1 2 3 4 5
--+------------
0 | A B C D E F
1 | G H I J K L
2 | M N O P Q R
3 | S T U V W X
4 | Y Z 0 1 2 3
5 | 4 5 6 7 8 9
```
> Please note, the _x_ and _y_ indices start at zero.

### Encryption
Encryption is done in six easy steps:

1. Convert the key and plain text symbol to its _x_ and _y_ positions
2. Add the keys _x_ position to the plain texts _x_ position
3. Add the keys _y_ position to the plain texts _y_ position
4. Divide the _x_ position by 6 and use the remainder as the new _x_ position
5. Divide the _y_ position by 6 and use the remainder as the new _y_ position
6. Convert the so calculated _x_ and _y_ positions to the cipher text symbol

_Repeat with the next symbol if needed._

#### Example
```
   H  E  L  L  O  Plain text as symbols
  11 04 15 15 22  Plain text as positions

   X  X  X  X  X  Key as symbols
+ 35 35 35 35 35  Key as positions

   Y  V  2  2  5  Cipher text as symbols
= 40 33 44 44 51  Cipher text as positions
```

### Decryption
Decryption is done in six easy steps:

1. Convert the key and cipher text symbol to its _x_ and _y_ positions
2. Substract the keys _x_ position from the cipher texts _x_ position
3. Substract the keys _y_ position from the cipher texts _y_ position
4. Divide the _x_ position by 6 and use the remainder as the new _x_ position
5. Divide the _y_ position by 6 and use the remainder as the new _y_ position
6. Convert the so calculated _x_ and _y_ positions to the plain text symbol

_Repeat with the next symbol if needed._

#### Example
```
   Y  V  2  2  5  Cipher text as symbols
  40 33 44 44 51  Cipher text as positions

   X  X  X  X  X  Key as symbols
- 35 35 35 35 35  Key as positions

   H  E  L  L  O  Plain text as symbols
= 11 04 15 15 22  Plain text as positions
```

### Key Generation
Key generation is done in three easy steps.

1. Throw a six-sided gambling dice, use the result minus 1 as the _x_ position
2. Throw a six-sided gambling dice, use the result minus 1 as the _y_ position
3. Convert the _x_ and _y_ positions to the key symbol

_Repeat with the next symbol if needed._

> It is advised to separate the key into blocks of five symbols for better
> readability and therefor a lesser chance of encryption/decryption errors.

### Security Considerations
There are a few points to consider, to ensure maximal confidentiality:

* Every key *must* be kept secret
* Every key *must not* be used twice
* Every partner *must* destroy the key after usage
* Only two partners *should* have the same key

## Usage
```$ practical.py COMMAND [KEY TEXT...]```

### Commands
* `-e` Encrypts the given text
* `-d` Decrypts the given text
* `-g` Generates a random key block
* `-h` Shows the usage text
* `-l` Shows the license
* `-v` Shows the version

### Examples
```$ practical.py -e XXXXX HELLO```

```$ practical.py -d XXXXX YV255```

```$ practical.py -g```

## Usage As Library
The Python modul exports the `Practical` class.

> Please note, that the key must have the same length as the text.

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

pt, k = "Hello", practical.generate(5)

ct = practical.encrypt(pt, k)
pt = practical.decrypt(ct, k)
```

### Unit Tests
For testing the [pytest](https://pytest.org/) modul is required.

```$ practical_test.py [...]```

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute
this software, either in source code form or as a compiled binary, for any
purpose, commercial or non-commercial, and by any means.

[Christian Uhsat](christian@uhsat.de)