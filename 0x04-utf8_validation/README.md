

# UTF-8 Validation

## Description

This project provides a method to determine if a given data set represents a valid UTF-8 encoding. The method checks the following criteria:

1. A character in UTF-8 can be 1 to 4 bytes long.
2. The data set can contain multiple characters.
3. The data is represented by a list of integers, where each integer represents 1 byte of data (you only need to handle the 8 least significant bits of each integer).
