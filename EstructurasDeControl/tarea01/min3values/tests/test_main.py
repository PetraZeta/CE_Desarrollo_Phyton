import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (7, 4, 9, 4),
    (2, 5, 1, 1),
    (9, 3, 7, 3),
    (9, 9, 9, 9),
]


@pytest.mark.parametrize('value1, value2, value3, expected', testdata)
def test_run(value1, value2, value3, expected):
    assert main.run(value1, value2, value3) == expected
