#!/usr/bin/env python3
import math

def convert_to_bits(n, pad):
    result = []
    while n > 0:
        if n % 2 == 0:
            result = [0] + result
        else:
            result = [1] + result
        n = math.floor(n / 2)
    while len(result) < pad:
        result = [0] + result
    return result

def string_to_bits(s):
    result = []
    for c in s:
        result = result + convert_to_bits(ord(c), 7)
    return result

def display_bits(b):
    bit_string = ''.join(map(str, b))
    print(bit_string)

def bits_to_char(b):
    assert len(b) == 7