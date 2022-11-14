from datetime import datetime

from date_utils import day_of_week


def test_monday_this_week_wednesday():
    """
    Returns midnight on Monday, given a datetime on Wednesday
    """
    wednesday_datetime = datetime(2022, 11, 16, 9, 10, 45, 23)
    monday_datetime = day_of_week.monday_this_week(wednesday_datetime)
    assert monday_datetime == datetime(2022, 11, 14, 0, 0, 0, 0)
