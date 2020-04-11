import sys
from math import log


DIGIT_MAP = {
    'zero': '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}


def convert(s):
    '''Converts a string representation of a set of digits to a number'''
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f'conversion error: {e!r}', file=sys.stderr)
        raise

def string_log(s):
    '''Outputs the log of a string representation of a number'''
    v = convert(s)
    return log(v)
