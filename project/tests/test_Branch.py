# project/tests

import unittest
import json

from project.tests.base import BaseTestCase

class TestBranchBlueprint(BaseTestCase):
    
    def test_create_branch(self):
        """ Tests inserting a branch into the db """
        with self.client:
            branch = 'Clareview'
            iLink = '1245'
            url = '/createBranch/' + branch + '/' \
                  + iLink

            create_response = self.client.post(
                url,
                content_type = 'application/json'
            )
            data = json.loads(create_response.data.decode())
            
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created branch.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

    def test_get_branch(self):
        """ Tests getting a branch from the db """
        with self.client:
            # Create branch to pull 
            branch = 'Clareview'
            iLink = '1245'
            url = '/createBranch/' + branch + '/' \
                  + iLink

            create_response = self.client.post(
                url,
                content_type = 'application/json'
            )
            data = json.loads(create_response.data.decode())
            
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created branch.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

            # Get the branch created
            get_response = self.client.get(
                '/getBranch',
                content_type = 'application/json'
            )
            data = json.loads(get_response.data.decode())
            return_query = data['data'][0]
            
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(return_query is not None)
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['iLink'] == '1245')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)
        
