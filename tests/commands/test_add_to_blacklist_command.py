import pytest
from unittest.mock import Mock
from src.commands.add_to_blacklist_command import AddToBlacklistCommand
from src.errors.errors import EmailAlreadyExists, InvalidParams


@pytest.fixture
def mock_db(monkeypatch):
    mocked_db = Mock()
    mocked_db.session.add.return_value = None
    mocked_db.session.commit.return_value = None
    monkeypatch.setattr('src.commands.add_to_blacklist_command.db', mocked_db)
    return mocked_db

@pytest.fixture
def mock_blacklist_entry(monkeypatch):
    mocked_entry = Mock()
    mocked_entry.query.filter_by.return_value.first.return_value = None
    monkeypatch.setattr('src.commands.add_to_blacklist_command.BlacklistEntry', mocked_entry)
    return mocked_entry


def test_add_blacklist_success(mock_db, mock_blacklist_entry):
    email = "test@example.com"
    app_uuid = "123"
    source_ip = "192.168.0.1"
    blocked_reason = "fraudulent activity"


    add_to_blacklist_command = AddToBlacklistCommand(email, app_uuid, source_ip, blocked_reason)
    command_response = add_to_blacklist_command.execute()

    assert type(command_response) == dict
    assert command_response == {"message": "Email added to the blacklist"}

def test_add_blacklist_missing_data(mock_db, mock_blacklist_entry):
    with pytest.raises(InvalidParams):
        add_to_blacklist_command = AddToBlacklistCommand(None, None, None, None)
        add_to_blacklist_command.execute()

def test_add_blacklist_already_exists(mock_db, mock_blacklist_entry):
    email = "test@example.com"
    app_uuid = "123"
    source_ip = "192.168.0.1"
    blocked_reason = "fraudulent activity"

    mock_blacklist_entry.query.filter_by.return_value.first.return_value = True
    with pytest.raises(EmailAlreadyExists):
        add_to_blacklist_command = AddToBlacklistCommand(email, app_uuid, source_ip, blocked_reason)
        add_to_blacklist_command.execute()