def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    if(day_of_week < 1 or day_of_week > 7):
        return None

    days = [None, 'Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']

    # print(days[day_of_week])

    return days[day_of_week]


weekday_name(1)
weekday_name(2)
weekday_name(3)
weekday_name(4)
weekday_name(5)
weekday_name(6)
