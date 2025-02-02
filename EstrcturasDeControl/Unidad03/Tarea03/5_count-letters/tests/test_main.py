import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('boom', {'b': 1, 'o': 2, 'm': 1}),
    ('ada', {'a': 2, 'd': 1}),
    ('tree', {'t': 1, 'r': 1, 'e': 2}),
    ('debugging', {'d': 1, 'e': 1, 'b': 1, 'u': 1, 'g': 3, 'i': 1, 'n': 1}),
    ('', {}),
]


@pytest.mark.parametrize('text, expected', testdata)
def test_run(text, expected):
    assert main.run(text) == expected
