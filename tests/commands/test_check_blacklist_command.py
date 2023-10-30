import pytest
from unittest.mock import Mock
from src.commands.check_blacklist_command import CheckBlacklistCommand


@pytest.fixture
def mock_blacklist_entry(monkeypatch):
    mocked_entry = Mock()
    mocked_entry.blocked_reason = "Test reason"
    mocked_entry.query.filter_by.return_value.first.return_value = mocked_entry
    monkeypatch.setattr('src.commands.check_blacklist_command.BlacklistEntry', mocked_entry)
    return mocked_entry


def test_check_blacklist_exists(mock_blacklist_entry):
    email = "test@example.com"
    check_blacklist_command = CheckBlacklistCommand(email)
    is_blocked, blocked_reason = check_blacklist_command.execute()

    assert is_blocked is True
    assert blocked_reason == "Test reason"


def test_check_blacklist_not_exists(monkeypatch):
    mocked_entry = Mock()
    mocked_entry.query.filter_by.return_value.first.return_value = None
    monkeypatch.setattr('src.commands.check_blacklist_command.BlacklistEntry', mocked_entry)

    email = "test@example.com"
    check_blacklist_command = CheckBlacklistCommand(email)
    is_blocked, blocked_reason = check_blacklist_command.execute()

    assert is_blocked is False
    assert blocked_reason is None
