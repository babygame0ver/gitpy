import requests , json
from gitpy.core.auth import GitPy
from gitpy.service.networkService import NetworkService
from gitpy.constants.urls import API_ENDPOINTS

class Repository():

    def __init__(self,authenticated_obj):
        self.gitpy_obj = authenticated_obj
        self.network_service = self.gitpy_obj.network_service
        self.api_endpoint = API_ENDPOINTS()
        
    def list_all_user_repositories(self):
        '''List all the repositories of User https://api.github.com/:user/repos '''           
        url = self.api_endpoint.get_url('repository_urls','all_repos',{})
        return self.network_service.get(url)

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
        url = self.api_endpoint.get_url('repository_urls','create_repo',{})
        return self.network_service.post(url,payload)

    def create_public_repository(self,repo_name):
        return self.create_repository(repo_name,False)

    def create_private_repository(self,repo_name):
        return self.create_repository(repo_name,True)

    def delete_repository(self,repo_name):
        params = {
            'username' : self.gitpy_obj.username,
            'repo_name' : repo_name
        }
        url = self.api_endpoint.get_url('repository_urls','repo_url',params)
        return self.network_service.delete(url)        
