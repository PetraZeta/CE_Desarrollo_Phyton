import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('CTRL', 'ALT', 'T', 'Open terminal'),
    ('CTRL', 'ALT', 'L', 'Lock screen'),
    ('CTRL', 'ALT', 'D', 'Show desktop'),
    ('ALT', 'F2', '', 'Run console'),
    ('CTRL', 'Q', '', 'Close window'),
    ('CTRL', 'ALT', 'DEL', 'Log out'),
    ('ALT', 'F2', 'Y', 'Undefined'),
    ('CTRL', 'Q', 'Z', 'Undefined'),
    ('CTRL', '', '', 'Undefined'),
    ('ALT', '', '', 'Undefined'),
    ('', '', '', 'Undefined'),
]


@pytest.mark.parametrize('key1, key2, key3, expected', testdata)
def test_run(key1, key2, key3, expected):
    assert main.run(key1, key2, key3) == expected
