# Write your code here
import requests


class JSONPlaceholder:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url
    def get_request(self):
        response = requests.get(self.base_url)
        return {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.content
        }
    def post_request(self, data):
        response = requests.post(self.base_url, json=data)
        return {
            "status_code": response.status_code,
            "headers": response.headers,
            "content": response.content
        }