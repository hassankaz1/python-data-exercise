import re


def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    lst = []
    vowels = 'aeiouAEIOU'
    for char in s:
        if(vowels.count(char) > 0):
            lst.append(char)

    str = ''
    for char in s:
        if(vowels.count(char) > 0):
            str = str + lst.pop()
        else:
            str = str + char
    return str


# reverse_vowels("hello!")
