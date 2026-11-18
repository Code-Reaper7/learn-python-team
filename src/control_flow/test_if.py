"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    elif number < 10:
        conclusion = 'Number is less than ten'
    elif number < 100:
        conclusion = 'Number is less than one hundred'
    else:
        conclusion = 'Number bigger than or equal to one hundred'

    assert conclusion == 'Number is less than one hundred'


def test_nested_if_statement():
    """Nested IF statement"""

    number = 8
    conclusion = ''

    if number > 0:
        if number % 2 == 0:
            conclusion = 'Positive even number'
        else:
            conclusion = 'Positive odd number'
    else:
        conclusion = 'Non-positive number'

    assert conclusion == 'Positive even number'


def test_multiple_elif_branches():
    """Multiple ELIF branches"""

    score = 76
    grade = ''

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    assert grade == 'C'

