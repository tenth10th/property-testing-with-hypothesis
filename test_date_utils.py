import date_utils
from datetime import datetime


def test_monday_this_week_wednesday():
    """
    Given any time this Wednesday, returns midnight on Monday
    """
    wednesday_datetime = datetime(2022, 11, 16, 9, 10, 45, 23)
    monday_datetime = date_utils.monday_this_week(wednesday_datetime)
    assert monday_datetime == datetime(2022, 11, 14, 0, 0, 0, 0)
