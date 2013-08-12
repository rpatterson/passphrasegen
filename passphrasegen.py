"""
Generate a passphrase consisting of words chosen from word list dictionaries.
"""

import math
import random
import argparse
import logging

parser = argparse.ArgumentParser(description=__doc__.strip())
parser.add_argument(
    'wordlist', nargs='+',
    help='one or more word list dictionaries with one word per line')
parser.add_argument(
    '-d', '--delimiter', default=' ',
    help='delimiter that separates the words in the passphrase'
    '(default: %(default)s)')
group = parser.add_mutually_exclusive_group()
group.add_argument(
    '-b', '--bits', type=float, default=128,
    help='minimum bits of entropy, determines the number of words '
    '(default: %(default)s)')
group.add_argument(
    '-l', '--length', type=int,
    help='length of the passphrase in number of words')

logger = logging.getLogger('passphrasegen')


def main(args=None, namespace=None):
    args = parser.parse_args(args, namespace)

    words = set()
    for wordlist in args.wordlist:
        words.update(
            word.strip().replace("'", "").lower() for word in open(wordlist))
    words = list(words)
    words_bits = math.log(len(words), 2)
    logger.info('The word lists have %s words with %s bits of entropy',
                len(words), round(words_bits, 1))

    if args.length:
        length = args.length
    else:
        length = int(math.ceil(args.bits / words_bits))
    bits = length * words_bits
    logger.info('The passphrase has %s words with %s bits of entropy',
                length, round(bits, 1))

    return args.delimiter.join(random.choice(words) for n in xrange(length))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print main()
