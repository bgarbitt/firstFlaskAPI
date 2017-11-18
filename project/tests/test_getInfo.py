# project/tests/test_getInfo.py

import unittest
import json
import time
import ast

from project.server import db
from project.tests.base import BaseTestCase

class TestGetInfoBlueprint(BaseTestCase):

    def test_Branch(self):
        with self.client:
            branch = 'Clareview'
            iLink = '1245'
            url = '/createBranch/' + branch + '/' \
                  + iLink

            create_response = self.client.post(
                url,
                content_type='application/json'
            )
            data=json.loads(create_response.data.decode())
            
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created branch.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

            get_response = self.client.get(
                '/getBranch',
                content_type='application/json'
            )
            data=json.loads(get_response.data.decode())
            query_output=ast.literal_eval(data['data'])[0]

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(query_output is not None)
            self.assertTrue(query_output['branch'] == 'Clareview')
            self.assertTrue(query_output['iLink'] == '1245')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

    def test_Zone(self):
        with self.client:
            branch = 'Clareview'
            iLink = '1245'
            url = '/createBranch/' + branch + '/' \
                  + iLink

            create_response = self.client.post(
                url,
                content_type='application/json'
            )
            data=json.loads(create_response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created branch.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

            beaconID='123456'
            zone='Landscapes'
            branch='Clareview'
            area='Nonfiction'
            color='Blue'
            url = '/createZone/' + beaconID + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + area + '/' \
                  + color
            
            create_response = self.client.post(
                url,
                content_type='application/json'
            )
            data = json.loads(create_response.data.decode())
            
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created zone.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

            get_response = self.client.get(
                '/getZone/' + branch,
                content_type='application/json'
            )
            data=json.loads(get_response.data.decode())
            query_output=ast.literal_eval(data['data'])[0]
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(query_output is not None)
            self.assertTrue(query_output['beaconID'] == '123456')
            self.assertTrue(query_output['zone'] == 'Landscapes')
            self.assertTrue(query_output['branch'] == 'Clareview')
            self.assertTrue(query_output['area'] == 'Nonfiction')
            self.assertTrue(query_output['color'] == 'Blue')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)
            
    def test_Question(self):
        with self.client:
            branch = 'Clareview'
            iLink = '1245'
            url = '/createBranch/' + branch + '/' \
                  + iLink

            create_response = self.client.post(
                url,
                content_type='application/json'
            )
            data=json.loads(create_response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created branch.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

            beaconID='123456'
            zone='Landscapes'
            branch='Clareview'
            area='Nonfiction'
            color='Blue'
            url = '/createZone/' + beaconID + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + area + '/' \
                  + color
            
            create_response = self.client.post(
                url,
                content_type='application/json'
            )
            data = json.loads(create_response.data.decode())
            
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created zone.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)
            
            prompt = 'question 1'
            choices = 'abcd'
            solution = 'a'
            zone = 'Landscapes'
            branch = 'Clareview'
            qtype = 'multChoice'
            ilink = '1'
            slink = '1'
            url = '/createQuestion/' + prompt + '/' \
                  + choices + '/' \
                  + solution + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + qtype + '/' \
                  + ilink + '/' \
                  + slink

            create_response = self.client.post(
                url,
                content_type='application/json'
            )
            data = json.loads(create_response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created question.')
            self.assertTrue(create_response.content_type == 'application/json')
            self.assertEqual(create_response.status_code, 201)

            url = '/getQuestion/' + zone + '/' \
                  + branch
            get_response = self.client.get(
                url,
                content_type='application/json'
            )
            data=json.loads(get_response.data.decode())
            query_output=ast.literal_eval(data['data'])[0]

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(query_output is not None)
            self.assertTrue(query_output['Prompt'] == 'question 1')
            self.assertTrue(query_output['Choices'] == 'abcd')
            self.assertTrue(query_output['Solution'] == 'a')
            self.assertTrue(query_output['zone'] == 'Landscapes')
            self.assertTrue(query_output['branch'] == 'Clareview')
            self.assertTrue(query_output['qType'] == 'multChoice')
            self.assertTrue(query_output['iLink'] == '1')
            self.assertTrue(query_output['sLink'] == '1')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

