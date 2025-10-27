#write your code here
import requests

# Helper class to wrap the response for attribute-style access
class ResponseWrapper:
    def __init__(self, status_code, headers=None, content=None):
        self.status_code = status_code
        self.headers = headers
        self.content = content

class JSONPlaceholder:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    # GET request
    def get_request(self):
        response = requests.get(self.base_url)
        return ResponseWrapper(
            status_code=response.status_code,
            headers=response.headers,
            content=response.text[:500]  # first 500 characters
        )

    # POST request
    def post_request(self, data):
        response = requests.post(self.base_url, json=data)
        return ResponseWrapper(
            status_code=response.status_code,
            headers=response.headers,
            content=response.text[:500]
        )

    # PUT request to update user
    def update_user(self, userId, title, body):
        data = {
            "title": title,
            "body": body
        }
        response = requests.put(f"{self.base_url}/{userId}", json=data)
        return ResponseWrapper(
            status_code=response.status_code,
            headers=response.headers,
            content=response.text[:500]
        )

    # DELETE request for a user
    def delete_user(self, userId):
        response = requests.delete(f"{self.base_url}/{userId}")
        return ResponseWrapper(
            status_code=response.status_code
        )

# Example usage
if __name__ == "__main__":
    json_placeholder = JSONPlaceholder()

    test_get = json_placeholder.get_request()
    print(test_get)  # <__main__.ResponseWrapper object at ...>
    print(test_get.status_code)  # e.g., 200

    post_data = {"title": "My POST request", "body": "bar", "userId": 1}
    practice_post = json_placeholder.post_request(post_data)
    print(practice_post)
    print(practice_post.status_code)  # e.g., 201

    update_user_4 = json_placeholder.update_user(4, "Test PUT", "This is new user 4 information")
    print(update_user_4)
    print(update_user_4.status_code)  # e.g., 200

    deleted_user = json_placeholder.delete_user(5)
    print(deleted_user)
    print(deleted_user.status_code)  # e.g., 200