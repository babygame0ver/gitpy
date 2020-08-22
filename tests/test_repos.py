import json ,logging , os , requests, unittest , namegenerator
from gitpy.core.auth import GitPy
from gitpy.repository.repos import Repository
from gitpy.constants.urls import api_urls
from gitpy.service.networkService import NetworkService
from .initial_setup import initial_config_setup

class TestRepository(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        ''' Setting up logger before testing whole script '''
        file_name = os.path.basename(__file__).split('.')[0]
        dir_path = os.path.dirname(os.path.realpath(__file__))
        log_file_path = os.path.join(dir_path, 'logs', file_name + '.log')
        cls.logger = logging.Logger(file_name)
        cls.logger.setLevel(logging.DEBUG)
        file_handle = logging.FileHandler(log_file_path)
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s: - %(message)s')
        file_handle.setFormatter(log_format)
        cls.logger.addHandler(file_handle)
        cls.logger.debug('Setting up Logger')
        cls.configuration_data = initial_config_setup()

    @classmethod
    def tearDownClass(cls):
        cls.logger.debug('Shutting down logger\n')

    def setUp(self):
        self.logger.info('executing')
        self.gitpy_object = GitPy(username=self.configuration_data['username'],token=self.configuration_data['token'])
        self.repository_object = Repository(self.gitpy_object)
        self.network_service = NetworkService(headers = {
            'Authorization' : 'Token {}'.format(self.gitpy_object.token)
        })
        self.repo_meta_data = {
          "description": "",
          "homepage": "",
          "has_issues": True,
          "has_projects": True,
          "has_wiki": True
        }
        self.repo_name = namegenerator.gen() 
        self.api_urls = api_urls()
        self.logger.info('completed')

    def test_list_all_repositories(self):
        self.logger.info('executing')        
        base_url = self.api_urls.get_url('repository_urls','all_repos',{})
        response = self.network_service.get(base_url)
        function_response = self.repository_object.list_all_user_repositories()
        self.assertEqual(json.dumps(response.json(),indent=2),
                         json.dumps(function_response.json(),indent=2),)
        self.logger.info('completed')

    def test_create_repository(self):        
        self.logger.info('executing')
        # Fake Random Repo Name        
        payload = {
            'username' : self.gitpy_object.username,
            'repo_name' : self.repo_name
        }        
        check_repo_url = self.api_urls.get_url('repository_urls','repo_url',payload)
        test_response = self.network_service.get(check_repo_url)
        # repo not exists in account
        self.assertEqual(test_response.status_code,404)
        function_response = self.repository_object.create_repository(self.repo_name,False)
        # repo created in account
        self.assertEqual(function_response.status_code,201)
        test_response = self.network_service.get(check_repo_url)
        # repo present in account
        self.assertEqual(test_response.status_code,200)
        function_response = self.repository_object.create_repository(self.repo_name,False)
        # repo already present in account
        self.assertEqual(function_response.status_code,422)   
        self.repository_object.delete_repository(self.repo_name)
        self.logger.info('completed')
        
    def test_delete_repository(self):        
        self.logger.info('executing')
        self.repository_object.create_repository(self.repo_name,False)                
        response = self.repository_object.delete_repository(self.repo_name)
        # deleted repository
        self.assertEqual(response.status_code,204)
        response = self.repository_object.delete_repository(self.repo_name)
        # repository not found hence can't be deleted 
        self.assertEqual(response.status_code,404)
        self.logger.info('completed')       
        
