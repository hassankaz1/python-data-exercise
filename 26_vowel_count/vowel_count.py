def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    new_dict = {}

    for i in phrase:
        if(vowels.count(i.lower()) > 0):
            if(new_dict.get(i.lower(), 0) > 0):
                new_dict[i.lower()] = new_dict[i.lower()]+1
            else:
                new_dict[i.lower()] = 1
    return new_dict
