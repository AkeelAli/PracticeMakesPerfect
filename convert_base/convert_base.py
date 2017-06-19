import string
from collections import namedtuple

def convert_to_decimal(num_as_str, base):
    is_negative = num_as_str[0] == '-'
    dec = 0 
    for c in num_as_str[is_negative:]:
        dec = dec*base + string.hexdigits.index(c.lower())
    dec = -1*dec if is_negative else dec
    return 0 if num_as_str == '0' else dec

'''
Convert from b1 to b2
'''
def convert_base(num_as_str, b1, b2):
    # First convert num to decimal base (x3x2x1x0 => x0 + x1*b1 + x2*b1^2 + x3*b1^3 = ((x3*b1 + x2)*b1 + x1)*b1) ===> multiply by b1, then add next digit, ...
    # Then convert decimal to b2 (x % b2 ==> digit, x // b2...)
    dec = convert_to_decimal(num_as_str, b1) 
    is_negative = dec < 0
    converted = ''
    dec = abs(dec)
    while dec:
        converted += string.hexdigits[dec % b2].upper()
        dec //= b2

    return ('-' if is_negative else '') + converted[::-1]


if __name__ == '__main__':
    assert 423 == convert_to_decimal('1A7', 16)

    Problem = namedtuple('Problem', ('num_as_str', 'b1', 'b2', 'result'))

    problems = [
        Problem('1A7', 16, 10, '423'),
        Problem('-25', 10, 16, '-19'),
        Problem('4', 16, 2, '100'),
    ]
    
    for p in problems:
        assert p.result == convert_base(*(p[:-1])), "Invalid result {} for problem {}".format(convert_base(*(p[:-1])), p)
