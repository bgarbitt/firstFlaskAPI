# project/tests

import unittest
import json

from project.tests.base import BaseTestCase

class TestZoneBlueprint(BaseTestCase):

    def test_create_zone(self):
        """ Tests inserting a zone into the db """
        with self.client:
            # Create a branch to satisify the
            # foreign key constraint
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

            # After the constraint is satisfied
            # create the zone
            beaconID = '123456'
            zone = 'Landscapes'
            branch = 'Clareview'
            area = 'Nonfiction'
            color = 'Blue'
            url = '/createZone/' + beaconID + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + area + '/' \
                  + color
            
            create_response = self.client.post(
                url,
                content_type ='application/json'
            )

            data = json.loads(create_response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created zone.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

    def test_get_zone(self):
        """ Tests getting a zone from the db """
        with self.client:
            # Create a branch to satisfy the
            # foreign key constraint
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

            # After the constraint is satisfied
            # create the zone
            beaconID = '123456'
            zone = 'Landscapes'
            branch = 'Clareview'
            area = 'Nonfiction'
            color = 'Blue'
            url = '/createZone/' + beaconID + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + area + '/' \
                  + color
            
            create_response = self.client.post(
                url,
                content_type = 'application/json'
            )
            
            data = json.loads(create_response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created zone.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

            # Get the zone created
            get_response = self.client.get(
                '/getZone/' + branch,
                content_type = 'application/json'
            )

            data = json.loads(get_response.data.decode())
            return_query = data['data'][0]
            
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(return_query is not None)
            self.assertTrue(return_query['beaconID'] == '123456')
            self.assertTrue(return_query['zone'] == 'Landscapes')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['area'] == 'Nonfiction')
            self.assertTrue(return_query['color'] == 'Blue')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)
