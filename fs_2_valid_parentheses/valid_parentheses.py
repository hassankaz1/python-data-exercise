def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    sum = 0

    for i in parens:
        if i == "(":
            sum += 1
        if i == ')':
            sum -= 1
        if(sum < 0):
            return False

    if(sum == 0):
        return True

    return False
