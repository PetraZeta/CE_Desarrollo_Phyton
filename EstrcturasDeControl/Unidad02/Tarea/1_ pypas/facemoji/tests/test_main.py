import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('happy', '😀'),
    ('sad', '😔'),
    ('angry', '😡'),
    ('pensive', '🤔'),
    ('surprised', '😮'),
    ('crazy', None),
]

for feeling, emoji in testdata[: len(testdata)]:
    testdata.append((feeling.upper(), emoji))


@pytest.mark.parametrize('feeling, expected', testdata)
def test_run(feeling, expected):
    assert main.run(feeling) == expected
