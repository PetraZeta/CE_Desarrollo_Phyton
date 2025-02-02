import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ({6, 12, 4, 50, 100}, {3, 2, 25}),
    ({42, 21, 14, 18, 7}, {9, 10, 3}),
    ({11, 8, 37, 21, 84, 5}, {2, 4, 10, 42, 18}),
    ({10, 4, 5}, {2}),
]


@pytest.mark.parametrize('values, expected', testdata)
def test_run(values, expected):
    assert main.run(values) == expected
