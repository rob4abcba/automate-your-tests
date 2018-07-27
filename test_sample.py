"""Automate your Tests Tutorial:

https://glenjarvis.com/interactions/automate-your-tests/
"""


def inc(initial_value):
    """Return arithmetic increase of 1 to initial_value"""
    return initial_value + 1


def test_answer():
    """Sample test for our repository

    We expect this test to pass
    """
    assert inc(3) == 5