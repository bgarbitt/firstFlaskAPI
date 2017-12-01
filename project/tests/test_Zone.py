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
            zone = 'Nonfiction'
            branch = 'Clareview'
            category = 'Mushrooms'
            color = 'Blue'
            url = '/createZone/' + beaconID + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + category + '/' \
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
            zone = 'Nonfiction'
            branch = 'Clareview'
            category = 'Mushrooms'
            color = 'Blue'
            url = '/createZone/' + beaconID + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + category + '/' \
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
            self.assertTrue(return_query['zone'] == 'Nonfiction')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['category'] == 'Mushrooms')
            self.assertTrue(return_query['color'] == 'Blue')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

    def test_delete_zone(self):
        """ Tests deleting a zone from the db """
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
            zone = 'Nonfiction'
            branch = 'Clareview'
            category = 'Mushrooms'
            color = 'Blue'
            url = '/createZone/' + beaconID + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + category + '/' \
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
            self.assertTrue(return_query['zone'] == 'Nonfiction')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['category'] == 'Mushrooms')
            self.assertTrue(return_query['color'] == 'Blue')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

            # Delete the zone
            delete_url = 'deleteZone/' + zone + '/' + branch

            delete_response = self.client.delete(
                delete_url,
                content_type = 'application/json'
            )
            data = json.loads(delete_response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully deleted zone.')
            self.assertTrue(delete_response.content_type == 'application/json')
            self.assertEqual(delete_response.status_code, 200)

            # Check zone was deleted
            get_response = self.client.get(
                '/getZone/' + branch,
                content_type = 'application/json'
            )

            data = json.loads(get_response.data.decode())
            
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(not data['data'])
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

    def test_update_zone(self):
        """ Tests updating a zone in the db """
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
            zone = 'Nonfiction'
            branch = 'Clareview'
            category = 'Mushrooms'
            color = 'Blue'
            
            url = '/createZone/' + beaconID + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + category + '/' \
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
            self.assertTrue(return_query['zone'] == 'Nonfiction')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['category'] == 'Mushrooms')
            self.assertTrue(return_query['color'] == 'Blue')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

            # Editing the zone for update
            beaconID = '123456 - changed'
            newZone = 'Nonfiction - changed'
            oldZone = 'Nonfiction'
            newBranch = 'Clareview'
            oldBranch = 'Clareview'
            category = 'Mushrooms - changed'
            color = 'Blue - changed'

            # Update zone
            url = '/updateZone/' + beaconID  + '/' \
                                 + oldZone   + '/' \
                                 + newZone   + '/' \
                                 + oldBranch + '/' \
                                 + newBranch + '/' \
                                 + category  + '/' \
                                 + color

            update_response = self.client.post(
                url,
                content_type = 'application/json'
            )
            data = json.loads(update_response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully updated zone.')
            self.assertTrue(update_response.content_type == 'application/json')
            self.assertEqual(update_response.status_code, 201)

            # Get the zone that was just updated
            url = '/getZone/' + newBranch

            get_response = self.client.get(
                url,
                content_type = 'application/json'
            )

            data = json.loads(get_response.data.decode())
            return_query = data['data'][0]

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(return_query is not None)
            self.assertTrue(return_query['beaconID'] == '123456 - changed')
            self.assertTrue(return_query['zone'] == 'Nonfiction - changed')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['category'] == 'Mushrooms - changed')
            self.assertTrue(return_query['color'] == 'Blue - changed')

            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

