import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('hello-world', False),
    ('Computer', True),
    ('first_in_first_out', False),
    ('Development', True),
    ('Programming is fun!', False),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
