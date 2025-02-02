import os

import pytest

if os.path.exists('solution.py'):
    import solution as main
else:
    import main  # type:ignore

testdata = [
    (
        33,
        47,
        """033 !   034 "   035 #   036 $   037 %
038 &   039 '   040 (   041 )   042 *
043 +   044 ,   045 -   046 .   047 /""",
    ),
    (
        58,
        87,
        """058 :   059 ;   060 <   061 =   062 >
063 ?   064 @   065 A   066 B   067 C
068 D   069 E   070 F   071 G   072 H
073 I   074 J   075 K   076 L   077 M
078 N   079 O   080 P   081 Q   082 R
083 S   084 T   085 U   086 V   087 W""",
    ),
    (
        98,
        117,
        """098 b   099 c   100 d   101 e   102 f
103 g   104 h   105 i   106 j   107 k
108 l   109 m   110 n   111 o   112 p
113 q   114 r   115 s   116 t   117 u""",
    ),
]


@pytest.mark.parametrize('start_code, end_code, expected', testdata)
def test_run(start_code, end_code, expected, capsys):
    main.run(start_code, end_code)
    captured = capsys.readouterr()
    expected_output = [line.strip() for line in expected.strip().split('\n')]
    captured_output = [line.strip() for line in captured.out.strip().split('\n')]
    assert expected_output == captured_output
