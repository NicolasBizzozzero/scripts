""" Generate random integers with a Linear Congruential Generator.
Defaults parameters are all suggested by gcc.
"""
import time
import argparse


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-s", '--seed', type=int, default=None,
                        help='seed used to start the generator. gcc defaults to time.time()')
    parser.add_argument('--modulus', type=int, default=2 ** 31,
                        help='modulus used in the generator. gcc defaults to 2^31')
    parser.add_argument('--multiplier', type=int, default=1103515245,
                        help='multiplier used in the generator. gcc defaults to 1103515245')
    parser.add_argument("-i", '--increment', type=int, default=12345,
                        help='increment used in the generator. gcc defaults to 12345')
    parser.add_argument("-n", '--n-values', type=int, default=1,
                        help='Number of values to generate. Set to negative for infinite values.')
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int(time.time())

    while args.n_values != 0:
        args.seed = linear_congruential_generator(args.seed, args.modulus, args.multiplier, args.increment)
        print(args.seed)
        args.n_values -= 1


def linear_congruential_generator(seed, modulus, multiplier, increment):
    """ Generate a sequence of numbers using a Linear Congruential Generator
    algorithm.
    :param seed: The first element of the sequence.
    :param modulus: The upper bound value of all numbers generated.
    :param multiplier:
    :param increment:
    :returns: A new `seed` parameter to use for the next generation.
    """
    assert 0 < modulus
    assert 0 < multiplier < modulus
    assert 0 < increment < modulus
    assert 0 < seed < modulus

    return ((multiplier * seed) + increment) % modulus


if __name__ == '__main__':
    main()
