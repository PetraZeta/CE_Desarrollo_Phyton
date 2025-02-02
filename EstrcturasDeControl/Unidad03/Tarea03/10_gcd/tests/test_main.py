import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (1, 1, 1),
    (3, 7, 1),
    (46, 64, 2),
    (12, 44, 4),
    (28, 91, 7),
    (48, 60, 12),
    (42, 56, 14),
]


@pytest.mark.parametrize('a, b, expected', testdata)
def test_run(a, b, expected):
    assert main.run(a, b) == expected
