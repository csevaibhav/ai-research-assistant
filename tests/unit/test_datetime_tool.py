from app.tools.datetime_tool import DateTimeTool


def test_datetime_tool_returns_string():

    tool = DateTimeTool()

    result = tool.execute()

    assert isinstance(result, str)

    assert len(result) > 0