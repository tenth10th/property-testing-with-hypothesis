from date_utils import time_since
from datetime import datetime
from hypothesis import given, assume
from hypothesis.strategies import datetimes
"""
In addition to the more traditional TDD style tests below,
what could Hypothesis do for us?
"""


def test_days_ago_1():
    current_datetime = datetime(2022, 11, 14, 20, 49)
    past_datetime = datetime(2022, 11, 13, 20, 45)
    days = time_since.days_ago(current_datetime, past_datetime)
    assert days == 1

def test_days_ago_2():
    current_datetime = datetime(2022, 11, 14, 20, 49)
    past_datetime = datetime(2022, 11, 13, 20, 55)
    days = time_since.days_ago(current_datetime, past_datetime)
    assert days == 0

@given(datetimes(), datetimes())
def test_days_ago_3(current_datetime, past_datetime):
    assume(current_datetime > past_datetime)
    days = time_since.days_ago(current_datetime, past_datetime)
    # assert abs(days) >= 0
    assert days >= 0

def test_hours_ago():
    #time_since.days_ago(current_datetime, past_datetime)
    # TODO: Implement this?
    pass

def test_years_ago():
    #time_since.years_ago(current_datetime, past_datetime)
    # TODO: Implement this?
    pass

def test_describe_time_since_current_just_now():
    #time_since.describe_time_since_current(current_datetime, past_datetime)
    # TODO: Implement this?
    pass

def test_describe_time_since_current_hours():
    #time_since.describe_time_since_current(current_datetime, past_datetime)
    # TODO: Implement this?
    pass

def test_describe_time_since_current_days_hours():
    #time_since.describe_time_since_current(current_datetime, past_datetime)
    # TODO: Implement this?
    pass

def test_describe_time_since_current_years_days_hours():
    #time_since.describe_time_since_current(current_datetime, past_datetime)
    # TODO: Implement this?
    pass


def test_describe_time_since():
    #time_since.describe_time_since(past_datetime)
    # TODO: Implement this, though probably not that necessary?
    pass
