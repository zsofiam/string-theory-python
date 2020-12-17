def is_palindrome(text):
    is_palindrome = True
    converted_text = ''.join([i for i in text if i.isalpha()]).upper()
    for i in range(len(converted_text)//2):
        if converted_text[i] != converted_text[len(converted_text)-1-i]:
            is_palindrome = False
            break
    return is_palindrome


def is_isogram(text):
    is_isogram = True
    converted_text = ''.join([i for i in text if i.isalpha()]).upper()
    appeared_letters = set()
    for letter in converted_text:
        if letter.upper() in appeared_letters:
            is_isogram = False
            break
        else:
            appeared_letters.add(letter.upper())
    return is_isogram


def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    pass


def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    pass


def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    pass


if __name__ == "__main__":
    print(is_palindrome("indul a gorog aludni"))
    print(is_palindrome("Mr. Owl ate my metal worm"))
    print(is_palindrome("op"))
    print(is_isogram('un3cop2yrighta3bles'))



