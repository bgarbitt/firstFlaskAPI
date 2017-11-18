# project/tests

import unittest
import json

from project.tests.base import BaseTestCase

class TestQuestionBlueprint(BaseTestCase):

    def test_create_question(self):
        """ Tests inserting a question into the db """
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

            # After the constraints for zone and branch
            # are satisfied, create the question
            prompt = 'question 1'
            choices = 'abcd'
            solution = 'a'
            zone = 'Landscapes'
            branch = 'Clareview'
            qtype = 'writInput'
            ilink = '1'
            slink = '1'
            blanks = 'a__d'
            url = '/createQuestion/' + prompt + '/' \
                  + choices + '/' \
                  + solution + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + qtype + '/' \
                  + ilink + '/' \
                  + slink + '/' \
                  + blanks

            create_response = self.client.post(
                url,
                content_type = 'application/json'
            )
            data = json.loads(create_response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created question.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

    def test_get_question(self):
        """ Tests getting a question from the db """
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

            # After the constraints for zone and branch
            # are satisfied, create the question
            prompt = 'question 1'
            choices = 'abcd'
            solution = 'a'
            zone = 'Landscapes'
            branch = 'Clareview'
            qtype = 'writInput'
            ilink = '1'
            slink = '1'
            blanks = 'a__d'
            url = '/createQuestion/' + prompt + '/' \
                  + choices + '/' \
                  + solution + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + qtype + '/' \
                  + ilink + '/' \
                  + slink + '/' \
                  + blanks

            create_response = self.client.post(
                url,
                content_type = 'application/json'
            )
            data = json.loads(create_response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created question.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

            # Get the question created
            url = '/getQuestion/' + zone + '/' \
                  + branch
            
            get_response = self.client.get(
                url,
                content_type = 'application/json'
            )
            
            data = json.loads(get_response.data.decode())
            return_query = data['data'][0]

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(return_query is not None)
            self.assertTrue(return_query['Prompt'] == 'question 1')
            self.assertTrue(return_query['Choices'] == 'abcd')
            self.assertTrue(return_query['Solution'] == 'a')
            self.assertTrue(return_query['zone'] == 'Landscapes')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['qType'] == 'writInput')
            self.assertTrue(return_query['iLink'] == '1')
            self.assertTrue(return_query['sLink'] == '1')
            self.assertTrue(return_query['blanks'] == 'a__d')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)
