import requests , json 
from time import sleep

class NetworkService():
    
    dev_api_v3 = 'https://api.github.com'
    
    def __init__(self,headers=None):
        self.headers = headers
        self.loader = 1
            
    def get(self,url):          
        self.base_url = self.getBaseUrl(url)  
        response = requests.get(self.base_url,headers=self.headers)        
        return response
    
    def post(self,url,payload):
        self.base_url = self.getBaseUrl(url)         
        response = requests.post(self.base_url,headers=self.headers,data=json.dumps(payload))        
        return response
        
    
    def delete(self,url):
        self.base_url = self.getBaseUrl(url)
        response = requests.delete(self.base_url,headers=self.headers)
        sleep(self.loader)
        return response
    
    def update(self,url,payload):
        pass
    
    def getBaseUrl(self,url):
        return f'{self.dev_api_v3}/{url}'