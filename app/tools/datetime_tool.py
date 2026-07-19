from datetime import datetime

from app.tools.base_tool import BaseTool


class DateTimeTool(BaseTool):
    """
    Tool that returns the current system date and time.
    """

    name = "datetime"

    description = (
        "Returns the current system date and time."
    )

    def execute(self, **kwargs):

        return datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )