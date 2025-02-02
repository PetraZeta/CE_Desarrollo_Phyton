import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('xy', '$#', 'x$x#y$y#'),
    ('abc', '123', 'a1a2a3b1b2b3c1c2c3'),
    ('ho', 'ho', 'hhhoohoo'),
    ('😀😡', '🤔😔', '😀🤔😀😔😡🤔😡😔'),
]


@pytest.mark.parametrize('text1, text2, expected', testdata)
def test_run(text1, text2, expected):
    assert main.run(text1, text2) == expected
