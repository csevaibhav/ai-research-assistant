from app.tools.calculator_tool import CalculatorTool


def test_calculator_addition():

    tool = CalculatorTool()

    result = tool.execute(
        expression="2 + 3"
    )

    assert result == "5"


def test_calculator_multiplication():

    tool = CalculatorTool()

    result = tool.execute(
        expression="10 * 4"
    )

    assert result == "40"


def test_calculator_invalid_expression():

    tool = CalculatorTool()

    try:
        tool.execute(expression="abc + xyz")
        assert False

    except ValueError:
        assert True