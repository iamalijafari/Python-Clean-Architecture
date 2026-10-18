from app.main import greet


def test_greet_returns_expected_message():
    result = greet("Ali")

    assert result == "Hello, Ali!"
