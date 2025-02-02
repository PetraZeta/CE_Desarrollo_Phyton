import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('lumberjacks', True),
    ('background', True),
    ('downstream', True),
    ('six-year-old', True),
    ('Circus', False),
    ('fantastical', False),
    ('left-hand-side', False),
    ('syMMetrical', False),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
