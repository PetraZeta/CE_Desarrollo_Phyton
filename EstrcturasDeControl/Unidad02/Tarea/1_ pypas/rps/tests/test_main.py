import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    # tie
    ('rock', 'rock', 0),
    ('paper', 'paper', 0),
    ('scissors', 'scissors', 0),
    # player1 wins
    ('scissors', 'paper', 1),
    ('rock', 'scissors', 1),
    ('paper', 'rock', 1),
    # player2 wins
    ('paper', 'scissors', 2),
    ('scissors', 'rock', 2),
    ('rock', 'paper', 2),
]

for p1, p2, result in testdata[: len(testdata)]:
    testdata.append((p1.upper(), p2.upper(), result))


@pytest.mark.parametrize('player1, player2, expected', testdata)
def test_run(player1, player2, expected):
    assert main.run(player1, player2) == expected
