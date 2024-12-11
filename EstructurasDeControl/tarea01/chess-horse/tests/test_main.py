import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (5, 4, 3),
    (8, 7, 5),
    (0, 0, 0),
    (6, 5, -1),
]


@pytest.mark.parametrize('target_x, target_y, expected', testdata)
def test_run(target_x, target_y, expected):
    assert main.run(target_x, target_y) == expected
