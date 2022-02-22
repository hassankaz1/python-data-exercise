def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    if(start == None):
        start = 0
    if(type(collection) == set):
        for element in collection:
            if(element == sought):
                return True
    elif(type(collection) == dict):
        for key, value in collection.items():
            if(key == sought or value == sought):
                return True
    else:
        for i in range(start, len(collection)):
            if(collection[i] == sought):
                return True
    return False


includes([1, 2, 3], 1)
includes([1, 2, 3], 1, 2)
includes("hello", "o")
includes(('Elmo', 5, 'red'), 'red', 1)
includes({1, 2, 3}, 1)
includes({1, 2, 3}, 1, 3)
includes({"apple": "red", "berry": "blue"}, "blue")
