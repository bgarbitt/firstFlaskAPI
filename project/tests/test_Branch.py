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

    def test_iLink_missing(self):
        """ Test inserting a branch into the db with a missing image link """
        with self.client:
            branch = 'Clareview'
            url = '/createBranch/' + branch

            create_response = self.client.post(
                url,
                content_type ='application/json'
            )
            data = json.loads(create_response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created branch.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)
            
    def test_delete_branch(self):
        """ Tests deleting a branch from the db """
        with self.client:
            # Create the branch to delete
            branch = "Clareview"
            iLink = "1245"
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

            # Delete the branch created
            delete_url = '/deleteBranch/' + branch

            delete_response = self.client.delete(
                delete_url,
                content_type = 'application/json'
            )
            data = json.loads(delete_response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully deleted branch.')
            self.assertTrue(delete_response.content_type == 'application/json')
            self.assertEqual(delete_response.status_code, 200)

            # Verify that there is no such branch
            get_response = self.client.get(
                '/getBranch',
                content_type = 'application/json'
            )
            data = json.loads(get_response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(not data['data'])
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)
            
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

    def test_get_branch_iLink(self):
        """ tests getting a branch from the db with a missing value """
        with self.client:
            branch = 'Clareview'
            url = '/createBranch/' + branch

            create_response = self.client.post(
                url,
                content_type = 'application/json'
            )
            data = json.loads(create_response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created branch.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

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
            self.assertTrue(return_query['iLink'] == '');
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

    def test_update_branch(self):
        """ Tests updating a branch from the db """
        with self.client:
            # Create the branch to delete
            branch = "Clareview"
            iLink = "1245"
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

            oldBranch = "Clareview"
            newBranch = "Clareview - changed"
            newiLink = "123456 - changed"

            url = '/updateBranch/' + oldBranch + '/' + newBranch + '/' + newiLink

            update_response = self.client.post(
                url,
                content_type = 'application/json'
            )
            data = json.loads(update_response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully updated branch.')
            self.assertTrue(update_response.content_type == 'application/json')
            self.assertEqual(update_response.status_code, 201)

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
            self.assertTrue(return_query['branch'] == 'Clareview - changed')
            self.assertTrue(return_query['iLink'] == '123456 - changed')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)
