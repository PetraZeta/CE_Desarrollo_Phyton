import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        None,
        """1
121
12321
1234321
123454321
12345654321
1234567654321
123456787654321
12345678987654321""",
    ),
]


@pytest.mark.parametrize('_, expected', testdata)
def test_run(_, expected, capsys):
    main.run()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
