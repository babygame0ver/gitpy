import requests , json
from gitpy.core.auth import GitPy
from gitpy.service.networkService import NetworkService

class RepositoryUrls():
    
    urls = {
        'all_repos' : 'user/repos',
        'create_repo' : 'user/repos',
        'repo_url' : 'repos/{}/{}'
    }
    
    @staticmethod
    def get_all_repo_url():
        return RepositoryUrls.urls['all_repos']
    
    @staticmethod
    def get_create_repo_url():
        return RepositoryUrls.urls['create_repo']
    
    @staticmethod
    def get_repo_url(username,repo):
        return RepositoryUrls.urls['repo_url'].format(username,repo)

class Repository():

    def __init__(self,authenticated_obj):
        self.gitpy_obj = authenticated_obj
        self.network_service = NetworkService(headers = {
            'Authorization' : 'Token {}'.format(self.gitpy_obj.token)
        })
        
    def list_all_user_repositories(self):
        '''List all the repositories of User https://api.github.com/:user/repos '''
        base_url = RepositoryUrls.get_all_repo_url()    
        return self.network_service.get(base_url)

    def create_post_data(self,repo_name,access = None):
        ''' https://developer.github.com/v3/repos/#create '''        
        repo_meta_data = {
          "name": "{}".format(repo_name),
          "description": "",
          "homepage": "",
          "has_issues": True,
          "has_projects": True,
          "has_wiki": True
        }
        if(access): # for private repo
            repo_meta_data["private"] = True
        return repo_meta_data

    def create_repository(self,repo_name,access):
        ''' Creating repository'''
        payload = self.create_post_data(repo_name,access)
        base_url = RepositoryUrls.get_create_repo_url()        
        return self.network_service.post(base_url,payload)

    def create_public_repository(self,repo_name):
        return self.create_repository(repo_name,False)

    def create_private_repository(self,repo_name):
        return self.create_repository(repo_name,True)

    def delete_repository(self,repo_name):
        base_url = RepositoryUrls.get_repo_url(self.gitpy_obj.username,repo_name)
        return self.network_service.delete(base_url)        

def main():
    pass

if __name__ == '__main__':
    main()
