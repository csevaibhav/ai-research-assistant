from tests.fakes.fake_provider import FakeProvider


def test_fake_provider_returns_expected_response():
    provider = FakeProvider()

    response = provider.generate("What is AI?")

    assert response == "This is a fake AI response."