import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (16, '0 3 6 9'),
    (45, '0 3 6 9 12 15'),
    (70, '0 3 6 9 12 15 18 21'),
]


@pytest.mark.parametrize('limit, expected', testdata)
def test_run(limit, expected, capsys):
    main.run(limit)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
