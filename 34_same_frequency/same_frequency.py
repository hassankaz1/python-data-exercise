def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    dict_one = {}
    dict_two = {}
    while(num1 > 0 and num2 > 0):
        temp_num_one = num1 % 10
        temp_num_two = num1 % 10

        if(dict_one.get(temp_num_one, 0) > 0):
            dict_one[temp_num_one] = dict_one[temp_num_one] + 1
        else:
            dict_one[temp_num_one] = 1

        if(dict_two.get(temp_num_two, 0) > 0):
            dict_two[temp_num_two] = dict_two[temp_num_two] + 1
        else:
            dict_two[temp_num_two] = 1

        num1 //= 10

        num2 //= 10

    if(num1 != num2):
        return False

    if dict_one != dict_two:
        return False

    return True
