import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('0001010011101', '0000110010001', 4),
    ('abc', 'abcd', -1),
    ('teclado', 'techado', 1),
    ('esperanza', 'esmeralda', 3),
]


@pytest.mark.parametrize('text1, text2, expected', testdata)
def test_run(text1, text2, expected):
    assert main.run(text1, text2) == expected
