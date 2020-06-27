import secrets

def xkcd_style_password(word_amount = 4, max_char = 25):
    with open('/usr/share/dict/words') as f:
        words = [word.strip() for word in f if len(word.strip()) <= max_char]
        password = ' '.join(secrets.choice(words) for i in range(word_amount))
        return password

