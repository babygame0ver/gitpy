import unittest
from unittest import mock
from unittest.mock import patch
from gitpy.repository.repos import Repository

class TestRepository(unittest.TestCase):

    def setUp(self):
        self.gitpyObj = mock.Mock()
        self.gitpyObj.network_service = ''
        self.repo = Repository(self.gitpyObj)

    @patch('gitpy.repository.repos.Repository.create_repository')
    def test_create_repository_success(self,mock_object):        
        mock_object.return_value.status_code = 201
        payload = {
            'username' : 'username',
            'repo_name' : 'reponame'
        }      
        response = self.repo.create_repository(payload)
        self.assertEqual(response.status_code,201)
    
    @patch('gitpy.repository.repos.Repository.create_repository')
    def test_duplicate_repository_exists(self,mock_object):        
        mock_object.return_value.status_code = 422
        payload = {
            'username' : 'username',
            'repo_name' : 'alreadypresentrepositoryname'
        }      
        response = self.repo.create_repository(payload)
        self.assertEqual(response.status_code,422)

    @patch('gitpy.repository.repos.Repository.delete_repository')
    def test_delete_repository_success(self,mock_object):
        mock_object.return_value.status_code = 204
        response = self.repo.delete_repository('repo-name-that-exists-in-user-account')
        self.assertEqual(response.status_code,204)
    
    @patch('gitpy.repository.repos.Repository.delete_repository')
    def test_delete_repository_failure(self,mock_object):
        mock_object.return_value.status_code = 404
        response = self.repo.delete_repository('repo-name-that-is-already-deleted-from-user-account')
        self.assertEqual(response.status_code,404)
