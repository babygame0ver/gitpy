
=========================================================
GitPy : Python Interface to GitHub's developer API
=========================================================

Overview :

A command line package purely written in Python3 consumes GitHub developer's API and provides all the functionalities in one place using Python Function.

* Core : Deals with authentication with GitHub API using Authentication token.

* Repository : Deals with information & actions related to both public & private Repositories.


1. Using Gitpy to Authenticate the username and token

.. code-block:: python

    from gitpy.core.auth import GitPy

    def authentication_module_using_configFile():
        config_data = GitPy.get_initial_configuration()
        print(config_data)
        print(g.check_connectivity()) # Connected
        print(g.authorization()) # Authorization Successfull {username}

    def authentication_module_using_Credentials(): # bad practice -> never hard-code username & token in file
        g = GitPy(username = 'username',token = 'token')
        print(g.check_connectivity()) # Connected
        print(g.authorization()) # Authorization Successfull {username}


    def main():
        authentication_module_using_configFile()
        authentication_module_using_Credentials()

    if __name__ == '__main__':
        main()

2. Using Repository module to create and delete Public/Private Repositories in account

.. code-block:: python

    from gitpy.repository.repos import Repository


    def RepositoryModule():

        r = Repository()
        print(r.list_all_user_repositories()) # JSON response
        print(r.create_public_repository('My-Public-Repository')) # public repository created
        print(r.create_private_repository('My-Private-Repository')) # private repository created
        print(r.delete_a_repository('My-Public-Repository')) # deleting repository 
        print(r.delete_a_repository('My-Private-Repository')) # deleting repository 


    def main():
        RepositoryModule()


    if __name__ == '__main__':
        main()
