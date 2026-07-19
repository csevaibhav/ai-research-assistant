import pytest

from app.tools.tool_executor import ToolExecutor


def test_execute_calculator_tool():

    result = ToolExecutor.execute(
        "calculator",
        expression="5 + 10"
    )

    assert result == "15"


def test_execute_datetime_tool():

    result = ToolExecutor.execute("datetime")

    assert isinstance(result, str)
    assert len(result) > 0


def test_unknown_tool():

    with pytest.raises(ValueError):
        ToolExecutor.execute("unknown_tool")