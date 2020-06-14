'''
Repository class deals with repository (public/private) creation/deletion/listing.
Response based function support. 
See list_all_repos(gitpy_object) for more information. 
'''

from gitpy.core.auth import GitPy
from gitpy.repository.repos import Repository
import json

def basic_authentication():
    # bad practice use env file or environment variables 
    username = 'myusername'
    token = 'myrandomtoken'
    g = GitPy(username,token)    
    return g

def list_all_repos(gitpy_object):
    repo = Repository(gitpy_object)
    response = repo.list_all_user_repositories()
    if(response.status_code == 200):
        print(json.dumps(response.json(),indent=2)) # all repo & meta-data
    else if (response.status_code == 401):        
        print('Bad credentials')
        
if __name__ == '__main__':
    gitpy_object = basic_authentication()
    list_all_repos(gitpy_object)