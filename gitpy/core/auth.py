import json , os , requests
from gitpy.service.networkService import NetworkService

class CoreUrls():
    
    urls = {
        'authUrl' : 'users/{}'
    }
    
    @staticmethod
    def getAuthUrl(username):
        return CoreUrls.urls['authUrl'].format(username)

class GitPy:
    
    def __init__(self,username=None,token=None):        
        self.username = username        
        self.token = token        
        self.network_service = NetworkService(headers = {
            'Authorization' : 'Token {}'.format(self.token)
        })

    @staticmethod
    def get_initial_configuration():
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        config_path = os.path.join(project_root,'config.json')
        if(os.path.exists(config_path)):
            with open(config_path,'r') as config_file:
                return json.loads(config_file.read())        
        else:
            return({ 'username' : os.environ['username'],
                     'token' : os.environ['token'] })                         

    def authenticate(self):
        url = CoreUrls.getAuthUrl(self.username)
        response = self.network_service.get(url)
        headers = response.headers        
        if headers['Status'] == "200 OK" and headers['X-RateLimit-Limit'] == "5000":
            return('Authentication Successfull blackhathack3r')
        if headers['Status'] == '401 Unauthorized':
            return('Access Denied : Wrong Token')
        if headers['Status'] == "404 Not Found":
            return('Access Denied : Wrong Username')        
        
def main():
    pass

if __name__ == '__main__':
    main()
