import unittest
from unittest.mock import patch
from gitpy.core.auth import GitPy


class TestAuth(unittest.TestCase):

    def setUp(self):
        self.gitpy_obj = g = GitPy("correctusername", "correcttoken")

    @patch("gitpy.core.auth.GitPy.authenticate")
    def test_authentication_success(self, mock_object):
        mock_object.return_value.status_code = 200
        mock_object.return_value.headers = {
            "status": "200 OK",
            "X-RateLimit-Limit": "5000",
        }
        response = self.gitpy_obj.authenticate()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["status"], "200 OK")
        self.assertEqual(response.headers["X-RateLimit-Limit"], "5000")

    @patch("gitpy.core.auth.GitPy.authenticate")
    def test_authentication_unauthorized(self, mock_object):
        mock_object.return_value.status_code = 401
        mock_object.return_value.headers = {
            "status": "401 Unauthorized",
            "X-RateLimit-Limit": "60",
        }
        response = self.gitpy_obj.authenticate()

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["status"], "401 Unauthorized")
        self.assertEqual(response.headers["X-RateLimit-Limit"], "60")

    @patch("gitpy.core.auth.GitPy.authenticate")
    def test_authentication_notfound(self, mock_object):
        mock_object.return_value.status_code = 404
        mock_object.return_value.headers = {
            "status": "404 Not found",
            "X-RateLimit-Limit": "60",
        }
        response = self.gitpy_obj.authenticate()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["status"], "404 Not found")
        self.assertEqual(response.headers["X-RateLimit-Limit"], "60")


if __name__ == "__main__":
    unittest.main()
