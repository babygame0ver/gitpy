'''
Repository class deals with repository (public/private) creation/deletion.
Response based function support. 
See repo_deletion(gitpy_object,repo_name) for more information. 
'''

from gitpy.core.auth import GitPy
from gitpy.repository.repos import Repository

def basic_authentication():
    # bad practice use env file or environment variables 
    username = 'myusername'
    token = 'myrandomtoken'
    g = GitPy(username,token)    
    return g

def repo_deletion(gitpy_object,repo_name):
    repo = Repository(gitpy_object)
    response = repo.delete_repository(repo_name)
    print(response.status_code) # 204 -> Success , 401 -> Not Allowed , 404 -> Repo not found

if __name__ == '__main__':
    gitpy_object = basic_authentication()
    repo_deletion(gitpy_object,'my-public-repo')