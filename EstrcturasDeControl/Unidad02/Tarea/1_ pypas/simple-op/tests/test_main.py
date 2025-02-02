import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (5, 2, '+', 7),
    (5, 2, '-', 3),
    (5, 2, '*', 10),
    (5, 2, '/', 2.5),
    (5, 2, '&', None),
]


@pytest.mark.parametrize('num1, num2, op, expected', testdata)
def test_run(num1, num2, op, expected):
    assert main.run(num1, num2, op) == expected
