
=========================================================
GitPy
=========================================================

Python Interface to GitHub's developer API


|Code Climate| |License| |Build Status| |Code Coverage|


.. |Code Climate| image:: https://codeclimate.com/github/babygame0ver/gitpy.png?style=flat-square
    :alt: Code Maintainability
    :scale: 100%
    :target: https://codeclimate.com/github/babygame0ver/gitpy
    
.. |License| image:: https://img.shields.io/badge/license-MIT%20License-green.svg
    :alt: License
    :scale: 100%
    :target: https://opensource.org/licenses/MIT

.. |Build Status| image:: https://api.travis-ci.com/babygame0ver/gitpy.svg
    :alt: Build Status
    :scale: 100%
    :target: https://app.travis-ci.com/github/babygame0ver/gitpy

.. |Code Coverage| image:: https://codecov.io/gh/babygame0ver/gitpy/graph/badge.svg?token=nDeQuSURqF 
:alt: Code Coverage
:scale: 100%
:target: https://codecov.io/gh/babygame0ver/gitpy

=========================================================
Dependencies
=========================================================

|python|  |Requests|

.. |python| image:: https://img.shields.io/badge/Python-3.7.4-blue.svg?style=flat-square
    :alt: Python version
    :scale: 100%
    :target: https://www.python.org/downloads/release/python-374/
    
.. |Requests| image:: https://img.shields.io/badge/Requests-2.22.0-blue.svg?style=flat-square
    :alt: Requests version
    :scale: 100%
    :target: (https://pypi.org/project/coverage/
    
=========================================================
Installation
=========================================================

.. code-block:: shell

    git clone https://github.com/babygame0ver/gitpy.git
    git checkout -b install
    python3 setup.py install


=========================================================
Introduction & Features
=========================================================

* GitPy provide response based object for the GitHub Developer's API with the help of methods.

* Response based approach helps other Developers to write their own logic after performing the action.

* To write your own application interacting with GitHub API you need to store the end-point urls & mock them using request library. GitPy takes care it for you.


=========================================================
Usage
=========================================================

Gitpy provides modules to interact with GitHub Developer API. These modules contain functions to return the response object which can be used to write your custom logic. 

Funtions are defined as per the operations.

**Authentication**

    * ``GitPy(username : String ,token : String)`` : Create a Gitpy Object to interact with GitHub API.

    * ``authenticate()`` : Verify the token authentication for a given username.

**Repository**

    * ``Repository(object : GitPy Object)`` : Creates a repository object to perform operations for repository. 

    * ``list_all_user_repositories()`` : List all the repository of a user.

    * ``create_public_repository(repository_name : String)`` : Creates a public repository with given repository name.

    * ``create_private_repository(repository_name : String)`` : Creates a private repository with given repository name.

    * ``create_repository(repository_name : String, access : Boolean)`` : Creates a repository with given repository name. True passed for access will create private repository vice versa.

    * ``delete_repository(repository_name : String)`` : Delete repository with given repository name.

=========================================================
Getting Started
=========================================================

Gitpy works with username & token of a given account. Please obtain a personal access token with all permissions & save it somewhere securely. 

`Github Personal Token Guide <https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line>`_	

1. **Authenticating username & token with Github API.**


.. code-block:: python2

    from gitpy.core.auth import GitPy

    def basic_authentication():
        # bad practice use env file or environment variables to secure your credentials.
        username = 'myusername'
        token = 'myrandomtoken'
        g = GitPy(username,token)    
        response = g.authenticate()
        headers = response.headers
        if(headers['status] == '200 OK' and headers['X-RateLimit-Limit'] === '5000'):
            print('Authentication Successfull')
        if(headers['status] == '401 Unauthorized'):
            print('Wrong Token provided')
        if(headers['status] == '404 Not Found'):
            print('Username not found')
        
    if __name__ == '__main__':
        basic_authentication()
    
2. **Creating Repositories.** 

.. code-block:: python2

    '''
    Repository Class deals with repository (public/private) creation/deletion.
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

3. **Repository Deletion.** 

.. code-block:: python2

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

4. **Listing all repositories.**

.. code-block:: python2

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

=========================================================
Development Setup
=========================================================

1. Running Tests & Development

.. code-block:: shell

    pip install -r requirements.txt
    python scripts/ci/run-tests 
    
=========================================================
 Support & Contribution
=========================================================

If you are facing issues related to bugs, code documentation, development setup or any other general issue.
Feel free to open an issue to reproduce the bug by providing sample code with proper label.   

Contributions are always welcome.

You can do any of these following:

1. What can you do ? : Improve code Readability, Maintainability, any implemetation that makes current project better, new ideas for the project.

2. How you can do it ? : Fork the repository, Implement new features by creating a seprate branch & sending PR to develop branch , with writting proper unit tests.  

Engineered with ❤️ by `babygame0ver <https://www.github.com/babygame0ver>`_
