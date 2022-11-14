from datetime import datetime, timedelta, time

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
# from hypothesis.extra import ghostwriter
# ghostwriter.idempotent(monday_this_week)


def days_ago(raw_datetime: datetime) -> int:
    difference: timedelta = datetime.now() - raw_datetime
    return difference.days

def days_ago(raw_datetime: datetime) -> int:
    difference: timedelta = datetime.now() - raw_datetime
    return difference.days


def describe_time_since(since_datetime: datetime) -> str:
    describe_strs = list()

    days_since = days_ago(since_datetime)
    if days_since:
        s = 's' if days_since != 1 else ''
        describe_strs.append(f"{days_since} day{s}")

    if describe_strs:
        return ", ".join(describe_strs) + " ago"
    else:
        return "today"
