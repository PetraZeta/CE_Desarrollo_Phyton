import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (-9, 9, (3, -6)),
    (-2, 0, (0, 3)),
    (4, 8, (4, -5)),
]


@pytest.mark.parametrize('x1, x2, expected', testdata)
def test_run(x1, x2, expected):
    assert main.run(x1, x2) == expected
