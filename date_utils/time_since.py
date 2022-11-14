from datetime import datetime, time, timedelta


def describe_time_since(past_datetime: datetime) -> str:
    """
    Describe the elapsed time since past_datetime in plain english
    e.g. "2 days, 12 hours ago", or "just now" if < 1 hour
    """
    current_datetime = datetime.now()
    return describe_time_since_current(current_datetime, past_datetime)


def describe_time_since_current(
    current_datetime: datetime, past_datetime: datetime
) -> str:
    """
    Describe the elapsed time between current_datetime and past_datetime
    (as per describe_time_since)
    """
    describe_strs = list()

    days_since = days_ago(current_datetime, past_datetime)
    if days_since:
        s = "s" if days_since != 1 else ""
        describe_strs.append(f"{days_since} day{s}")

    if describe_strs:
        return ", ".join(describe_strs) + " ago"
    else:
        return "recently"


def days_ago(current_datetime: datetime, past_datetime: datetime) -> int:
    """
    Return number of full days between current_datetime and past_datetime
    (or 0 if less than one day)
    """
    difference: timedelta = current_datetime - past_datetime
    return difference.days


def hours_ago(current_datetime: datetime, since_datetime: datetime) -> int:
    """
    Return number of full hours between current_datetime and past_datetime
    (or 0 if less than one hour)
    """
    difference: timedelta = current_datetime - since_datetime
    hour_in_seconds = 3_600
    if difference.seconds >= hour_in_seconds:
        return int(difference.seconds / hour_in_seconds)
    return 0


def years_ago(current_datetime: datetime, since_datetime: datetime) -> int:
    """
    Return number of full years between current_datetime and past_datetime
    (or 0 if less than one year)
    """
    difference: timedelta = current_datetime - since_datetime
    year_in_days = 365
    if difference.days > year_in_days:
        return int(difference.days / year_in_days)
    return 0
