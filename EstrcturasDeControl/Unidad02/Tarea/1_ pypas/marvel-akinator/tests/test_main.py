import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (True, True, True, 'Ironman'),
    (True, True, False, 'Captain Marvel'),
    (True, False, True, 'Ronan Accuser'),
    (True, False, False, 'Vision'),
    (False, True, True, 'Spiderman'),
    (False, True, False, 'Hulk'),
    (False, False, True, 'Black Bolt'),
    (False, False, False, 'Thanos'),
]


@pytest.mark.parametrize('can_fly, is_human, has_mask, expected', testdata)
def test_run(can_fly, is_human, has_mask, expected):
    assert main.run(can_fly, is_human, has_mask) == expected
