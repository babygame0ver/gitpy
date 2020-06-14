import json ,os

def initial_config_setup():
    ''' Setting up config file path env'''   
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(project_root,'config.json')
    if(os.path.exists(config_path)):
        with open(config_path,'r') as config_file:
            return json.loads(config_file.read())        
    else:
        return ({
                'username' : os.environ['username'],
                'token' : os.environ['token'] 
                })
            
        
            