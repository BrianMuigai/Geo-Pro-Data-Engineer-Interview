# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_none, assert_list_equal


# Local imports...
from tests.test_json import get_data

@patch('project.services.requests.get')
def test_getting_todos_when_response_is_ok(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]

    # Configure the mock to return a response with an OK status code. Also, the mock should have
    # a `json()` method that returns a list of todos.
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = get_data

    # Call the service, which will send a request to the server.
    response = {}

    # If the request is sent successfully, then I expect a response to be returned.
    assert_list_equal(response.json(), todos)
