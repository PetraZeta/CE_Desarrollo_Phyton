import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        87,
        ('50', '100', '90', '87'),
        """Introduzca número:
Mayor
Introduzca número:
Menor
Introduzca número:
Menor
Introduzca número:
Enhorabuena has encontrado el número en 4 intentos""",
    ),
    (
        7,
        ('1', '2', '3', '4', '8', '7'),
        """Introduzca número:
Mayor
Introduzca número:
Mayor
Introduzca número:
Mayor
Introduzca número:
Mayor
Introduzca número:
Menor
Introduzca número:
Enhorabuena has encontrado el número en 6 intentos""",
    ),
    (
        99,
        ('99',),
        """Introduzca número:
Enhorabuena has encontrado el número en 1 intentos""",
    ),
    (
        0,
        ('-1', '8', '5', '-7', '0'),
        """Introduzca número:
Mayor
Introduzca número:
Menor
Introduzca número:
Menor
Introduzca número:
Mayor
Introduzca número:
Enhorabuena has encontrado el número en 5 intentos""",
    ),
]


@pytest.mark.parametrize('target_number, inputs, expected', testdata)
def test_run(target_number, inputs, expected, monkeypatch, capsys):
    def gen_input():
        yield from inputs

    test_inputs = gen_input()

    def monkey_input(msg: str) -> str:
        print(msg.strip())
        return next(test_inputs)

    monkeypatch.setattr('builtins.input', monkey_input)
    main.run(target_number)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
