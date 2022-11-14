from datetime import datetime

from date_utils import day_of_week


def test_monday_this_week_wednesday():
    """
    Returns midnight on the same day, given a datetime on a Monday
    """
    # TODO: Implement basic unit tests
    # day_of_week.monday_this_week()
    pass

def test_monday_this_week_wednesday():
    """
    Returns midnight on Monday that week, given a datetime on a Wednesday
    """
    # TODO: Implement basic unit tests
    # day_of_week.monday_this_week()
    pass


"""
How could Hypothesis test our function more thoroughly?
"""
def test_monday_this_week_thoroughly():
    # TODO: Do cool hypothesis stuff here
    pass


"""
How could we confirm that `monday_this_week` is idempotent?
(That calling it 1 time or N times on the same date has the same effect?)

# from hypothesis.extra import ghostwriter
# print(ghostwriter.idempotent(date_utils.monday_this_week))
"""
def test_monday_this_week_is_idempotent():
    # TODO: Do cool hypothesis stuff here
    pass
