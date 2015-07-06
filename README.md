# Practical ![Build](https://travis-ci.org/cuhsat/practical.svg)
The Practical Cipher `0.1.2`

A one-time pad variant for easy manual application. Based on a 6x6 conversion
table supporting alphanumeric symbols. Random key generation can be done with
one normal gambling dice (d6).

An implementation in pure [Python](https://www.python.org) is provided.

## Specification

### Conversion Table
The conversion table uses a 6x6 alphanumeric matrix. It is filled from left
to right and from top to bottom with the uppercase latin letters of the
alphabet from `A` to `Z` and than the numbers from `0` to `9`.

> Please note, the _x_ and _y_ indices start at zero.

The conversion table with the default symbol arrangement:
```
    0 1 2 3 4 5

0   A B C D E F
1   G H I J K L
2   M N O P Q R
3   S T U V W X
4   Y Z 0 1 2 3
5   4 5 6 7 8 9
```
### Encryption
Encryption is done in six easy steps:

1. Convert the key and plain text symbol to its _x_ and _y_ positions
2. Add the keys _x_ position to the plain texts _x_ position
3. Add the keys _y_ position to the plain texts _y_ position
4. Divide the _x_ position by 6 and use the remainder as the new _x_ position
5. Divide the _y_ position by 6 and use the remainder as the new _y_ position
6. Convert the so calculated _x_ and _y_ positions to the cipher text symbol

Repeat with the next symbol if needed.

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

Repeat with the next symbol if needed.

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
Key generation is done in three easy steps:

1. Throw a six-sided gambling dice, use the result minus 1 as the _x_ position
2. Throw a six-sided gambling dice, use the result minus 1 as the _y_ position
3. Convert the _x_ and _y_ positions to the key symbol

Repeat with the next symbol if needed.

> It is advised to separate the key into blocks of five symbols for better
> readability and therefor a lesser chance of encryption/decryption errors.

For more information on randomness, please see [1].

#### On Distribution
Key distribution should be done directly after the key generation. It is
advised to create the keys by hand. Write down the generated keys to two
pieces of paper or books. The pages can be marked with page numbers for
easier locating of the key blocks later.

> It is advised to not use a computer system or any other electronic device to
> generate or distribute the keys.

#### On Synchronization
In order for both peers to refer to the same key, the keys to use must be 
synchronized between each message. The simplest way to do so is using a key 
book and referring to the used key by the page number.

### Security Considerations
There are a few points to consider, to ensure maximal confidentiality:

* Every key *must* be kept secret
* Every key *must not* be used twice
* Every peer *must* destroy the key directly after usage
* Only two peers *should* have the same key

## Usage As Executable
```$ practical.py COMMAND [KEY TEXT...]```

### Commands
* `-b, --generate-block` Generates a random key block
* `-p, --generate-page ` Generates a random key page
* `-d, --decrypt` Decrypts the given text
* `-e, --encrypt` Encrypts the given text

### Examples
```$ practical.py --encrypt XXXXX HELLO```

```$ practical.py --decrypt XXXXX YV255```

```$ practical.py --generate-block```

```$ practical.py --generate-page```

## Usage As Library
The Python modul exports the `Practical` class.

### Practical.encrypt(text, key)
Returns the given `text` encrypted with the given `key` as string.

> Please note, that the key must have the same length as the text.

### Practical.decrypt(text, key)
Returns the given `text` decrypted with the given `key` as string.

> Please note, that the key must have the same length as the text.

### Practical.generate_block(size)
Returns a new random key block of the given `size` as string.

### Practical.generate_page(size, cols, rows)
Returns a new random key page with the given `size`, `cols`, `rows` as string.

### Example
```python
from practical import Practical

cipher = Practical()

text, key = "Hello", cipher.generate_block(5)

text = cipher.encrypt(text, key)
text = cipher.decrypt(text, key)
```

### Unit Tests
The [pytest](https://pytest.org/) modul is required for unit testing.

```$ practical_test.py [...]```

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute
this software, either in source code form or as a compiled binary, for any
purpose, commercial or non-commercial, and by any means.

[Christian Uhsat](https://github.com/cuhsat), June 2015

----
[1] [Randomness for crypto](https://www.cs.berkeley.edu/~daw/rnd/)
