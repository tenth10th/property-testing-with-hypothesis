from datetime import datetime, time, timedelta


def monday_this_week(current_datetime: datetime) -> datetime:
    """
    Return midnight on Monday of the week this Datetime is in
    (Assumes weeks start on Monday, as per Python datetimes)
    """
    monday_datetime = current_datetime.combine(current_datetime, time())
    day_index = current_datetime.weekday()
    if day_index != 0:
        monday_datetime = monday_datetime - timedelta(days=day_index)
    return monday_datetime


# How could we test if monday_this_week is idempotent?
# Running it once produces the same output as running it N times?
#
# import date_utils
# from hypothesis.extra import ghostwriter
# print(ghostwriter.idempotent(date_utils.monday_this_week))
