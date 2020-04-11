import sys


def sqrt(x):
    '''Compute the square roots using the method of 
    Heron of Alexandria

    Args:
        X: The number for which the square root is 
        to be calculated.
    Returns:
        The square root of x.
    Raises:
        ValueError: If x is negative
    '''
    if x < 0:
        raise ValueError('Cannot compute square root of '
        f'negative number {x}')

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        nums = [9, 2, -1]
        for num in nums:
            print(sqrt(num))
    except ValueError as e:
        print(f'Error: {e!r}', file=sys.stdout)


if __name__ == "__main__":
    main()