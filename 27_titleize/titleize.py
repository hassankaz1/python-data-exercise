def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_str = phrase[0].upper()
    for i in range(1, len(phrase)):
        if(phrase[i-1] == ' '):
            new_str = new_str + phrase[i].upper()
        else:
            new_str = new_str + phrase[i].lower()

    return new_str
