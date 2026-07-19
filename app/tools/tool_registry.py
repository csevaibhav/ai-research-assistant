from app.tools.calculator_tool import CalculatorTool
from app.tools.datetime_tool import DateTimeTool


class ToolRegistry:
    """
    Central registry for all available tools.
    """

    _TOOLS = {
        "calculator": CalculatorTool,
        "datetime": DateTimeTool,
    }

    @classmethod
    def get_tool(cls, tool_name: str):

        if tool_name not in cls._TOOLS:
            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        return cls._TOOLS[tool_name]

    @classmethod
    def list_tools(cls):

        return list(cls._TOOLS.keys())