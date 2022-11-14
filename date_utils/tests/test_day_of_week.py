from datetime import datetime

from date_utils import day_of_week


def test_monday_this_week_wednesday():
    """
    Returns midnight on Monday, given a datetime on Wednesday
    """
    # day_of_week.monday_this_week(wednesday_datetime)
    pass

"""
How could Hypothesis test our function more thoroughly?
"""


"""
How could we confirm that `monday_this_week` is idempotent?
(That calling it 1 time or N times on the same date has the same effect?)

# from hypothesis.extra import ghostwriter
# print(ghostwriter.idempotent(date_utils.monday_this_week))
"""

