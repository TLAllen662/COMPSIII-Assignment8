# Write your code here
import requests

#create JSONPlaceholder class
class JSONPlaceholder:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url
#define get_request
def get_request(self):
    response = requests.get(self.base_url)
    return {
        "status_code": response.status_code,
        "headers": response.headers,
        "content": response.text[:500]  # first 500 characters
    }
#define post_request
def post_request(self, data):
    response = requests.post(self.base_url, json=data)
    return {
        "status_code": response.status_code,
        "headers": response.headers,
        "content": response.text[:500]
    }
#create put_request
def put_request(self, data):
        response = requests.put(self.base_url, json=data)
        return {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.content
        }
def update_user(self, userId, title, body):
    data = {
        "title": title,
        "body": body
    }
    response = requests.put(f"{self.base_url}/{userId}", json=data)
    return {
        "status_code": response.status_code,
        "headers": response.headers,
        "content": response.text[:500]
    }
#create delete_request
def delete_user(self, userId):
    response = requests.delete(f"{self.base_url}/{userId}")
    return {"status_code": response.status_code}