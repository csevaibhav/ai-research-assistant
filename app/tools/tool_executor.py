from app.tools.tool_registry import ToolRegistry


class ToolExecutor:
    """
    Executes registered tools.
    """

    @staticmethod
    def execute(tool_name: str, **kwargs):
        """
        Execute a registered tool.

        Args:
            tool_name: Name of the tool to execute.
            **kwargs: Arguments passed to the tool.

        Returns:
            Result returned by the tool.
        """

        tool_class = ToolRegistry.get_tool(tool_name)

        tool = tool_class()

        return tool.execute(**kwargs)