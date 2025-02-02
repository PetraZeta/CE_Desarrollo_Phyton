import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ([4, 3, 7, 3, 3, 1, 4, 6], [4, 3, 7, 1, 6]),
    ([2, 3, 2, 2, 1, 5, 4, 2, 4, 9], [2, 3, 1, 5, 4, 9]),
    ([0, 9, 0, 9, 0, 9], [0, 9]),
    ([1, 2, 3, 4, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize('nums_dups, expected', testdata)
def test_run(nums_dups, expected):
    assert main.run(nums_dups) == expected
