def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    new_dict = {}

    for char in phrase:
        if(char in new_dict):
            new_dict[char] = new_dict[char] + 1
        else:
            new_dict[char] = 1

    return new_dict
