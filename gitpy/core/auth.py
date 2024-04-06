import json, os, requests
from gitpy.service.networkService import NetworkService
from gitpy.constants.urls import API_ENDPOINTS


class GitPy:

    def __init__(self, username=None, token=None):
        self.username = username
        self.token = token
        self.network_service = NetworkService(
            headers={"Authorization": "Token {}".format(self.token)}
        )
        self.api_urls = API_ENDPOINTS()

    def authenticate(self):
        payload = {"username": self.username}
        url = self.api_urls.get_url("auth_urls", "authentication", payload)
        try:
            response = self.network_service.get(url)
            return response
        except requests.exceptions:
            return requests.exceptions
