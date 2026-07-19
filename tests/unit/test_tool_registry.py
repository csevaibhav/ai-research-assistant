from app.tools.tool_registry import ToolRegistry


def test_registry_returns_calculator_tool():

    tool = ToolRegistry.get_tool("calculator")

    assert tool.__name__ == "CalculatorTool"


def test_registry_returns_datetime_tool():

    tool = ToolRegistry.get_tool("datetime")

    assert tool.__name__ == "DateTimeTool"


def test_registry_lists_all_tools():

    tools = ToolRegistry.list_tools()

    assert "calculator" in tools
    assert "datetime" in tools