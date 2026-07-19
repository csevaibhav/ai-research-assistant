from app.tools.base_tool import BaseTool


class CalculatorTool(BaseTool):
    """
    Tool for evaluating simple mathematical expressions.
    """

    name = "calculator"

    description = (
        "Evaluates mathematical expressions such as "
        "2 + 3 * 5 or (10 - 4) / 2."
    )

    def execute(self, **kwargs):

        expression = kwargs.get("expression")

        if not expression:
            raise ValueError("Expression is required.")

        try:
            result = eval(expression, {"__builtins__": {}}, {})

            return str(result)

        except Exception as exc:
            raise ValueError(
                f"Invalid mathematical expression: {expression}"
            ) from exc