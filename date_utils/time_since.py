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
    # FIXME: Needs better implementation
    return "just now"


def days_ago(current_datetime: datetime, past_datetime: datetime) -> int:
    """
    Return number of full days between current_datetime and past_datetime
    (or 0 if less than one day)
    """    
    return (current_datetime - past_datetime).days


def hours_ago(current_datetime: datetime, since_datetime: datetime) -> int:
    """
    Return number of full hours between current_datetime and past_datetime
    (or 0 if less than one hour)
    """
    # FIXME: Needs better implementation
    return 0


def years_ago(current_datetime: datetime, since_datetime: datetime) -> int:
    """
    Return number of full years between current_datetime and past_datetime
    (or 0 if less than one year)
    """
    # FIXME: Needs better implementation
    return 0
