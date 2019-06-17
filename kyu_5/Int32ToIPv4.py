import math
import re


# https://www.codewars.com/kata/int32-to-ipv4/train/python
# function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
def int32_to_ip(int32):
    bits = int32_to_bits(int32)
    return bits_to_bytes(bits)


def bits_to_bytes(bits):
    result = ""
    octets = re.findall('........', bits)
    for octet in octets:
        sum = 0
        octet = octet[::-1]
        idx = 0
        while idx <= 7:
            if octet[idx] == '1':
                sum += math.pow(2, idx)
            idx += 1
        result = result + str(int(sum)) + "."
    return result[:-1]


def int32_to_bits(int32):
    power = 31
    result = ""
    while power >= 0:
        exp = math.pow(2, power)
        if exp <= int32:
            int32 = int32 - exp
            result = result + "1"
        else:
            result = result + "0"
        power = power - 1
    return result
