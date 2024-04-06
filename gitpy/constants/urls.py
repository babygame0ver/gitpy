class API_ENDPOINTS:
    def __init__(self):
        self.urls = {
            "auth_urls": Authentication.urls,
            "repository_urls": Repository.urls,
        }

    def get_url(self, module, action, payload):
        return self.urls[module][action].format(**payload)


class Authentication:
    urls = {"authentication": "users/{username}"}


class Repository:
    urls = {
        "all_repos": "user/repos",
        "create_repo": "user/repos",
        "repo_url": "repos/{username}/{repo_name}",
    }
