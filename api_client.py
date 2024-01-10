import requests
import json


class BlogClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def register(self, username, email, password):
        url = f"{self.base_url}/api/users/register/"
        data = {"username": username, "email": email, "password": password}
        response = requests.post(url, data=data)
        return response.json()

    def login(self, email, password):
        url = f"{self.base_url}/api/users/login/"
        data = {"email": email, "password": password}
        response = requests.post(url, data=data)
        self.token = response.json().get("access")
        return response.json()

    def get_posts(self):
        url = f"{self.base_url}/api/blog/posts/"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def verify_email(self, email):
        url = f"{self.base_url}/api/email/verify-email/"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json={"email": email}, headers=headers)
        if response.status_code == 200:
            try:
                return response.json()
            except json.JSONDecodeError:
                return {"error": "Response is not in JSON format"}
        else:
            return {
                "error": "Received a non-200 HTTP status",
                "status_code": response.status_code,
            }

    def get_email_result(self, email):
        url = f"{self.base_url}/api/email/email-result/"
        response = requests.get(url, params={"email": email})
        return response.json()


client = BlogClient("http://localhost:8000")
print(client.register("newuser", "newuser@example.com", "password123"))
print(client.login("newuser@example.com", "password123"))
print(client.get_posts())

valid_email = "test@example.com"
print(f"Testing verification of valid e-mail: {valid_email}")
valid_email_result = client.verify_email(valid_email)
print(valid_email_result)

email_to_check = "test@example.com"
email_result = client.get_email_result(email_to_check)
print(email_result)
