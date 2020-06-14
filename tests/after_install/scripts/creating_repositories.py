'''
Repository class deals with repository (public/private) creation/deletion.
Response based function support. 
See create_repository(gitpy_object) for more information. 
'''

from gitpy.core.auth import GitPy
from gitpy.repository.repos import Repository

def basic_authentication():
    # bad practice use env file or environment variables 
    username = 'myusername'
    token = 'myrandomtoken'
    g = GitPy(username,token)    
    return g

def create_repository(gitpy_object):
    repo = Repository(gitpy_object)
    response = repo.create_public_repository('my-public-repo')
    print(response.status_code) # 201 -> Created , 422 -> Already Present

    ''' or directy accessing underlying function '''
    response = repo.create_repository('my-public-repo-2',False)  # False for Public
    print(response.status_code) # 201 -> Created , 422 -> Already Present

    response = repo.create_private_repository('my-private-repo')
    print(response.status_code) # 201 -> Created , 422 -> Already Present

    ''' or directy accessing underlying function '''
    response = repo.create_repository('my-private-repo-2',True)  # True for Private
    print(response.status_code) # 201 -> Created , 422 -> Already Present


if __name__ == '__main__':
    gitpy_object = basic_authentication()
    create_repository(gitpy_object)