import json , os , requests
from gitpy.service.networkService import NetworkService
from gitpy.constants.urls import api_urls

class GitPy:
    
    def __init__(self,username=None,token=None):        
        self.username = username        
        self.token = token        
        self.network_service = NetworkService(headers = {
            'Authorization' : 'Token {}'.format(self.token)
        })
        self.api_urls = api_urls()

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
        payload = {'username' : self.username}
        url = self.api_urls.get_url('auth_urls','authentication',payload)
        return self.network_service.get(url)
