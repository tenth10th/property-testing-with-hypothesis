from datetime import datetime

from date_utils import day_of_week

from hypothesis import given
from hypothesis.strategies import datetimes

def test_monday_this_week_wednesday():
    """
    Returns midnight on Monday that week, given a datetime on a Wednesday
    """
    some_datetime = datetime(2022, 11, 16, 11, 24)
    monday_datetime = day_of_week.monday_this_week(some_datetime)
    assert monday_datetime == datetime(2022, 11, 14)


"""
How could Hypothesis test our function more thoroughly?
"""
@given(datetimes())
def test_monday_this_week_thoroughly(some_datetime):
    expected_monday = day_of_week.monday_this_week(some_datetime)
    print(f"\nHypothesis: {some_datetime}, => {expected_monday}")
    # This is Python's opinion, don't @ me
    MONDAY = 0
    assert expected_monday.weekday() == MONDAY

# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import date_utils.day_of_week
from hypothesis import given, strategies as st

@given(current_datetime=st.datetimes())
def test_idempotent_monday_this_week(current_datetime):
    result = date_utils.day_of_week.monday_this_week(current_datetime=current_datetime)
    repeat = date_utils.day_of_week.monday_this_week(current_datetime=result)
    assert result == repeat, (result, repeat)
    print(f"Hypothesis Idempotent: {result} == {repeat}")