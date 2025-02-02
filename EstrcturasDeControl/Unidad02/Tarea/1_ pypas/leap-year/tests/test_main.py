import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (1900, False),
    (1904, True),
    (1983, False),
    (1992, True),
    (2000, True),
    (2002, False),
    (2052, True),
    (2100, False),
]


@pytest.mark.parametrize('year, expected', testdata)
def test_run(year, expected):
    assert main.run(year) == expected
