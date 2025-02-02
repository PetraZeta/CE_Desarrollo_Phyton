import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([4, 3, 8, 1], [9, 2, 7, 3], 101),
    ([9, 1, 2], [8, 7, 5], 89),
    ([8, 3, 5, 6, 4], [3, 7, 7, 9, 3], 146),
    ([4, 2], [8, 7, 3], None),
]


@pytest.mark.parametrize('u, v, expected', testdata)
def test_run(u, v, expected):
    assert main.run(u, v) == expected
