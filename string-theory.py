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
    is_pangram = False
    converted_text = ''.join([i for i in text if i.isalpha()]).upper()
    letters_in_text = set(converted_text.upper())
    letters_in_alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    if letters_in_text == letters_in_alphabet:
        is_pangram = True
    return is_pangram


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
    print(is_pangram('The q1uick brown fox jumps2 over the9lazy dog'))
    print(is_pangram('aSphitnx of black quartttttz, judge my votw'))



