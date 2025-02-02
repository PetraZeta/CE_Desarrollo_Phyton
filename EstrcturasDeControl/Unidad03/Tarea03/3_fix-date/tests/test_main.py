import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    ('12/31/23', 2000, '31-12-2023'),
    ('2/21/15', 1800, '21-02-1815'),
    ('10/1/87', 1900, '01-10-1987'),
    ('9/29/1', 1700, '29-09-1701'),
    ('12/25/34', 500, '25-12-0534'),
]


@pytest.mark.parametrize('input_date, base_year, expected', testdata)
def test_run(input_date, base_year, expected):
    assert main.run(input_date, base_year) == expected
