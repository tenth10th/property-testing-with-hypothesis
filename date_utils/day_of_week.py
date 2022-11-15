from datetime import datetime, time, timedelta


def monday_this_week(current_datetime: datetime) -> datetime:
    """
    Return midnight on Monday of the week this Datetime is in
    (Assumes weeks start on Monday, as per Python datetimes)
    """
    days = current_datetime.weekday()
    delta = timedelta(days = days)
    monday_datetime = current_datetime - delta
    midnight_time = time()
    midnight_monday_datetime = datetime.combine(monday_datetime, midnight_time)
    return midnight_monday_datetime

"""
See tests/test_day_of_week for more activities...
"""