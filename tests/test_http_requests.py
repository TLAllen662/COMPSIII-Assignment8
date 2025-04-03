import pytest
from http_requests import JSONPlaceholder
from unittest.mock import Mock

@pytest.fixture
def json_placeholder():
    base_url = "https://jsonplaceholder.typicode.com/posts"
    return JSONPlaceholder(base_url)

@pytest.fixture
def mock_response(mocker):
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.headers = {"Content-Type": "application/json"}
    mock_resp.content = b'[{"userId": 1, "id": 1, "title": "test title", "body": "test body"}]'
    mocker.patch('requests.get', return_value=mock_resp)
    return mock_resp

@pytest.fixture
def mock_post_response(mocker):
    mock_resp = Mock()
    mock_resp.status_code = 201
    mock_resp.headers = {"Content-Type": "application/json"}
    mock_resp.content = b'{"userId": 1, "id": 101, "title": "foo", "body": "bar"}'
    mocker.patch('requests.post', return_value=mock_resp)
    return mock_resp

# Can create class
def test_jsonplaceholder_initialization(json_placeholder):
    """Test if JSONPlaceholder class is initialized correctly with base_url"""
    assert isinstance(json_placeholder, JSONPlaceholder)
    assert json_placeholder.base_url == "https://jsonplaceholder.typicode.com/posts"

def test_get_request_success(json_placeholder, mock_response):
    """Test if get_request method returns correct data structure with expected values"""
    result = json_placeholder.get_request()
    
    # Check if the result contains all expected keys
    assert isinstance(result, dict)
    assert all(key in result for key in ['status_code', 'headers', 'content'])
    
    # Check if the values are correct
    assert result['status_code'] == 200
    assert result['headers'] == {"Content-Type": "application/json"}
    assert result['content'] == b'[{"userId": 1, "id": 1, "title": "test title", "body": "test body"}]'

def test_get_request_with_correct_url(json_placeholder, mocker):
    """Test if get_request method calls requests.get with the correct URL"""
    mock_get = mocker.patch('requests.get')
    url = "https://jsonplaceholder.typicode.com/posts"
    
    json_placeholder.get_request()
    
    mock_get.assert_called_once_with(url)

def test_get_request_by_userid_success(json_placeholder, mock_response):
    """Test if get_request_by_userid method returns correct data structure"""
    url = "https://jsonplaceholder.typicode.com/posts"
    user_id = 3
    result = json_placeholder.get_request_by_userid(user_id)
    
    assert isinstance(result, dict)
    assert all(key in result for key in ['status_code', 'headers', 'content'])
    assert result['status_code'] == 200
    assert result['headers'] == {"Content-Type": "application/json"}

def test_get_request_by_userid_correct_parameters(json_placeholder, mocker):
    """Test if get_request_by_userid method calls requests.get with correct parameters"""
    mock_get = mocker.patch('requests.get')
    url = "https://jsonplaceholder.typicode.com/posts"
    user_id = 3
    
    json_placeholder.get_request_by_userid(user_id)
    
    # Check if the method was called with correct URL and parameters
    mock_get.assert_called_once_with(f'{url}?userId={user_id}')

def test_post_request_success(json_placeholder, mock_post_response):
    """Test if post_request method returns correct data structure"""
    url = "https://jsonplaceholder.typicode.com/posts"
    post_data = {"title": "foo", "body": "bar", "userId": 1}
    result = json_placeholder.post_request(post_data)
    
    assert isinstance(result, dict)
    assert all(key in result for key in ['status_code', 'headers', 'content'])
    assert result['status_code'] == 201  # POST typically returns 201 Created
    assert result['headers'] == {"Content-Type": "application/json"}
    assert result['content'] == b'{"userId": 1, "id": 101, "title": "foo", "body": "bar"}'

def test_post_request_correct_parameters(json_placeholder, mocker):
    """Test if post_request method calls requests.post with correct parameters"""
    mock_post = mocker.patch('requests.post')
    url = "https://jsonplaceholder.typicode.com/posts"
    post_data = {"title": "foo", "body": "bar", "userId": 1}
    
    json_placeholder.post_request(post_data)
    
    # Check if the method was called with correct URL and data
    mock_post.assert_called_once_with(url, data=post_data)

def test_update_user_success(json_placeholder, mocker):
    """Test successful PUT request to update a user"""
    # Mock the PUT response
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.headers = {"Content-Type": "application/json"}
    mock_resp.content = b'{"userId": 3, "id": 3, "title": "My test", "body": "Testing for user 3"}'
    mocker.patch('requests.put', return_value=mock_resp)
    
    result = json_placeholder.update_user(3, "My test", "Testing for user 3")
    
    # Verify response structure and content
    assert isinstance(result, dict)
    assert all(key in result for key in ['status_code', 'headers', 'content'])
    assert result['status_code'] == 200
    assert result['headers'] == {"Content-Type": "application/json"}
    assert result['content'] == b'{"userId": 3, "id": 3, "title": "My test", "body": "Testing for user 3"}'

def test_update_user_correct_url_and_data(json_placeholder, mocker):
    """Test if update_user makes PUT request with correct URL and data"""
    mock_put = mocker.patch('requests.put')
    user_id = 3
    title = "My test"
    body = "Testing for user 3"
    expected_data = {"title": title, "body": body}
    
    json_placeholder.update_user(user_id, title, body)
    
    # Verify the PUT request was made with correct URL and data
    expected_url = f"{json_placeholder.base_url}/{user_id}"
    mock_put.assert_called_once_with(expected_url, expected_data)

def test_delete_user_success(json_placeholder, mocker):
    """Test successful DELETE request"""
    # Mock the DELETE response
    mock_resp = Mock()
    mock_resp.status_code = 200
    mocker.patch('requests.delete', return_value=mock_resp)
    
    result = json_placeholder.delete_user(3)
    
    # Verify response structure and content
    assert isinstance(result, dict)
    assert 'status_code' in result
    assert result['status_code'] == 200

def test_delete_user_correct_url(json_placeholder, mocker):
    """Test if delete_user makes DELETE request with correct URL"""
    mock_delete = mocker.patch('requests.delete')
    user_id = 3
    
    json_placeholder.delete_user(user_id)
    
    # Verify the DELETE request was made with correct URL
    expected_url = f"{json_placeholder.base_url}/{user_id}"
    mock_delete.assert_called_once_with(expected_url)