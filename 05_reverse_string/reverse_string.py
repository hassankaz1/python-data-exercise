def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    lst = list(phrase)
    lst.reverse()

    string = ''.join(char for char in lst)

    return string
