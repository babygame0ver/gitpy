class api_urls:
    
    def __init__(self):
        self.urls = {
            'auth_urls' : auth_urls.urls,
            'repository_urls' : repository_urls.urls
        }

    def get_url(self,module,action,payload):
        return self.urls[module][action].format(**payload)

class auth_urls:
    urls = {
        'authentication' : 'users/{username}'
    }

class repository_urls:
    urls = {
        'all_repos' : 'user/repos',
        'create_repo' : 'user/repos',
        'repo_url' : 'repos/{username}/{repo_name}'
    }
