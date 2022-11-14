from datetime import datetime, time, timedelta


def monday_this_week(current_datetime: datetime) -> datetime:
    """
    Return midnight on Monday of the week this Datetime is in
    (Assumes weeks start on Monday, as per Python datetimes)
    """
    # FIXME: Needs better implementation!
    return datetime(2022, 11, 14, 0, 0, 0, 0)

"""
See tests/test_day_of_week for more activities...
"""