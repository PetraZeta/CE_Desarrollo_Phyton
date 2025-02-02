import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        None,
        """0|0 0|1 0|2 0|3 0|4 0|5 0|6
1|1 1|2 1|3 1|4 1|5 1|6
2|2 2|3 2|4 2|5 2|6
3|3 3|4 3|5 3|6
4|4 4|5 4|6
5|5 5|6
6|6""",
    ),
]


@pytest.mark.parametrize('_, expected', testdata)
def test_run(_, expected, capsys):
    main.run()
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    expected_lines = expected.strip().split('\n')
    for captured_line, expected_line in zip(captured_lines, expected_lines):
        assert captured_line.strip() == expected_line.strip()
