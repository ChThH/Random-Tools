import secrets
import argparse


def xkcd_style_password(word_amount=4, min_char=1, max_char=24):
    if max_char < min_char:
        print(
            'Maximum character value ({max}) cannot be less than minimum character value ({min}).'.format(max=max_char,
                                                                                                          min=min_char)
        )
        quit()
    try:
        with open('/usr/share/dict/words') as f:
            words = [word.strip() for word in f if (len(word.strip()) <= max_char and len(word.strip()) >= min_char)]
            password = ' '.join(secrets.choice(words) for i in range(word_amount))
        return password
    except IndexError:
        print('No words in that range of min/max characters.')
        quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    This script rolls a number of variable sided dice. 
    """)
    parser.add_argument("--words", help="Number of words", default=4, type=int)
    parser.add_argument("--min_char", help="Minimum amount of characters per word", default=1, type=int)
    parser.add_argument("--max_char", help="Maximum amount of characters per word", default=24, type=int)

    args = parser.parse_args()

    number = args.words
    min_char = args.min_char
    max_char = args.max_char

    result = xkcd_style_password(number, min_char, max_char)
    print(result)
