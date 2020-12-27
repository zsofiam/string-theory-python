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
    is_anagram = False
    dictionary1 = convert_text_to_dictionary(text1)
    dictionary2 = convert_text_to_dictionary(text2)
    if dictionary1 == dictionary2:
        is_anagram = True
    return is_anagram


def convert_text_to_dictionary(text):
    converted_text = ''.join([i for i in text if i.isalpha()]).upper()
    dictionary_of_letters = {}
    for char in converted_text:
        if char in dictionary_of_letters:
            dictionary_of_letters[char] += 1
        else:
            dictionary_of_letters[char] = 1
    return dictionary_of_letters


def is_blanagram(text1, text2):
    is_blanagram = False
    dictionary1 = convert_text_to_dictionary(text1)
    dictionary2 = convert_text_to_dictionary(text2)
    count_miss_1 = 0
    count_miss_2 = 0
    value_of_miss_1 = 0
    value_of_miss_2 = 0
    for letter in dictionary1:
        if letter not in dictionary2:
            count_miss_1 += 1
            value_of_miss_1 = dictionary1[letter]
    for letter in dictionary2:
        if letter not in dictionary1:
            count_miss_2 += 1
            value_of_miss_2 = dictionary2[letter]
    if count_miss_1 == count_miss_2 == 1 and value_of_miss_1 == value_of_miss_2:
        is_blanagram = True
    return is_blanagram


if __name__ == "__main__":
    print(is_blanagram('chipotle', "poetical"))



