import pytest

from app.app import hello


@pytest.mark.parametrize(
    "test_input,expected",
    [
        pytest.param("Happy path", "Hello, World!Happy path", id="Happy path"),
        pytest.param("mad", "Hello, World!mad", id="Not right"),
        pytest.param("angry", "Hello, World!angry", id="Not happy"),
    ],
)
def test_current_customer_logic(monkeypatch, test_input, expected):
    # Arrange
    monkeypatch.setenv("some_env", "n/a for this test")

    # Act
    actual = hello(test_input)

    # Assert
    assert actual == expected
