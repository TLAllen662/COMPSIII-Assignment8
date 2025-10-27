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
            "content": response.content
        }
#define post_request
    def post_request(self, data):
        response = requests.post(self.base_url, json=data)
        return {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.content
        }
#create put_request
    def put_request(self, data):
        response = requests.put(self.base_url, json=data)
        return {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.content
        }
    def update_user(userId, title, body):
        data = {
            "userId": userId,
            "title": title,
            "body": body
        response = requests.put(f"{self.base_url}/posts/{userId}", json=data)
        return {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.content
        }
        }
#create delete_request
    def delete_request(self):
        response = requests.delete(self.base_url)
        return {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.content
        }