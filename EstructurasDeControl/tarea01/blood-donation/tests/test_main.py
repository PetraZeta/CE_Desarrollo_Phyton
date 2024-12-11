import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (34, 81, 70, 151_000, True),
    (17, 81, 70, 200_000, False),
    (50, 47, 70, 171_000, False),
    (50, 47, 70, 128_000, False),
    (19, 86, 90, 210_000, True),
    (19, 86, 120, 210_000, False),
]


@pytest.mark.parametrize('age, weight, heartbeat, platelets, expected', testdata)
def test_run(age, weight, heartbeat, platelets, expected):
    assert main.run(age, weight, heartbeat, platelets) == expected
