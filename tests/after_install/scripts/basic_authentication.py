from gitpy.core.auth import GitPy

def basic_authentication():
    # bad practice use env file or environment variables 
    username = 'myusername'
    token = 'myrandomtoken'
    g = GitPy(username,token)    
    print(g.authenticate()) # Authentication successfull myusername / Access Denied : ( Wrong Token / Wrong Username ) 

if __name__ == '__main__':
    main()