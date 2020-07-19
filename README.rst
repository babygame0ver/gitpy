
=========================================================
GitPy
=========================================================

Python Interface to GitHub's developer API

------------
|build-status| |Code Climate| |Code Coverage| |Codacy Badge| |License|
------------


.. |build-status| image:: https://travis-ci.org/babygame0ver/gitpy.svg?branch=release&style=flat-square
    :alt: Travis Build Status
    :scale: 100%
    :target: https://travis-ci.org/babygame0ver/gitpy

.. |Code Climate| image:: https://codeclimate.com/github/babygame0ver/gitpy.png?style=flat-square
    :alt: Code Maintainability
    :scale: 100%
    :target: https://codeclimate.com/github/babygame0ver/gitpy
    
.. |Code Coverage| image:: https://codecov.io/gh/babygame0ver/gitpy/branch/release/graph/badge.svg
    :alt: Code Coverage
    :scale: 100%
    :target: https://codecov.io/gh/babygame0ver/gitpy
    
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/64422e753f1d40c9a7cc039b21f4363a
    :alt: Code Quality
    :scale: 100%
    :target: https://www.codacy.com/manual/babygame0ver/gitpy

.. |License| image:: https://img.shields.io/badge/license-MIT%20License-green.svg
    :alt: License
    :scale: 100%
    :target: https://opensource.org/licenses/MIT

=========================================================
Dependencies
=========================================================

------------
 |python|  |Requests| |Coverage| |Codecov| |NameGenerator|
------------

.. |python| image:: https://img.shields.io/badge/Python-3.7.4-blue.svg?style=flat-square
    :alt: Python version
    :scale: 100%
    :target: https://www.python.org/downloads/release/python-374/
    
.. |Requests| image:: https://img.shields.io/badge/Requests-2.22.0-blue.svg?style=flat-square
    :alt: Requests version
    :scale: 100%
    :target: (https://pypi.org/project/coverage/
    
.. |Coverage| image:: https://img.shields.io/badge/Coverage-4.5.4-blue.svg?style=flat-square
    :alt: Coverage version
    :scale: 100%
    :target: https://pypi.org/project/coverage/

.. |Codecov| image:: https://img.shields.io/badge/Codecov-4.5.4-blue.svg?style=flat-square
    :alt: Codecov version
    :scale: 100%
    :target: (https://pypi.org/project/codecov/
    
.. |NameGenerator| image:: https://img.shields.io/badge/Namegenerator-1.0.6-blue.svg?style=flat-square
    :alt: Codecov version
    :scale: 100%
    :target: https://pypi.org/project/namegenerator/
    

=========================================================
Installation
=========================================================

.. code-block:: shell

    git clone https://github.com/babygame0ver/gitpy.git
    git checkout -b install
    python3 setup.py install
    
=========================================================
Docs
=========================================================

Gitpy works with username & token of a given account. Please obtain a personal access token with all permissions & save it somewhere securely. 

`Github Personal Token Guide <https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line>`_	


1. **Authenticating username & token with Github API.**

.. code-block:: python

    from gitpy.core.auth import GitPy

    def basic_authentication():
        # bad practice use env file or environment variables 
        username = 'myusername'
        token = 'myrandomtoken'
        g = GitPy(username,token)    
        print(g.authenticate()) # Authentication successfull myusername 
        # OR Access Denied : ( Wrong Token / Wrong Username ) 

    if __name__ == '__main__':
        main()
    
2. **Creating Repositories.** 

.. code-block:: python

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

3. **Repository Deletion.** 

.. code-block:: python

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

.. code-block:: python

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

1. Obtain a personal access token with all permissions from github.

`Github Personal Token Guide <https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line>`_

2. Create a config.json file in root directory of project with following content.

.. code-block:: json

    {
    "username" : "username",
    "token" : "token"
    }
3. For Travis setup add username & token to your env variables.

4. Run Tests

.. code-block:: shell

    python3 -m unittest discover
    coverage run -m unittest discover
    
=========================================================
 Support
=========================================================

If you feel any point is missing out or don't find anything in the docs. Please create an issue with proper label and I will try my best to assist you there.

=========================================================
Contribution
=========================================================

Contributions are always welcome. Feel free to fork the repository

You can do any of these 

1. Improve code Readability , Maintainability or any implemetation that makes it better

2. Implement new features by creating a seprate branch & sending PR to develop branch.

or any other ideas which you feel makes it better. 
