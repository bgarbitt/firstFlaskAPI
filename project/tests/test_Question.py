#project/tests

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

            # After the constraints for zone and branch
            # are satisfied, create the question
            prompt = 'question 1'
            choices = 'abcd'
            solution = 'a'
            zone = 'Nonfiction'
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

            # After the constraints for zone and branch
            # are satisfied, create the question
            prompt = 'question 1'
            choices = 'abcd'
            solution = 'a'
            zone = 'Nonfiction'
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
            self.assertTrue(return_query['zone'] == 'Nonfiction')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['qType'] == 'writInput')
            self.assertTrue(return_query['iLink'] == '1')
            self.assertTrue(return_query['sLink'] == '1')
            self.assertTrue(return_query['blanks'] == 'a__d')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

    def test_get_all_questions(self):
        """ Tests getting all questions from the db """
        with self.client:
            # Create two branches to satisfy the
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

            branch = 'Clareview2'
            iLink = '12456'
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

            # After the constraint is satisfied
            # create the zone
            beaconID = '1234567'
            zone = 'Nonfiction'
            branch = 'Clareview2'
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


            # After the constraints for zone and branch
            # are satisfied, create the question
            prompt = 'question 1'
            choices = 'abcd'
            solution = 'a'
            zone = 'Nonfiction'
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

            prompt = 'question 1'
            choices = 'abcd'
            solution = 'a'
            zone = 'Nonfiction'
            branch = 'Clareview2'
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
            url = '/getAllQuestions/'

            get_response = self.client.get(
                url,
                content_type = 'application/json'
            )

            data = json.loads(get_response.data.decode())
            return_query1 = data['data'][0]
            return_query2 = data['data'][1]

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(return_query1 is not None)
            self.assertTrue(return_query1['Prompt'] == 'question 1')
            self.assertTrue(return_query1['Choices'] == 'abcd')
            self.assertTrue(return_query1['Solution'] == 'a')
            self.assertTrue(return_query1['zone'] == 'Nonfiction')
            self.assertTrue(return_query1['branch'] == 'Clareview')
            self.assertTrue(return_query1['qType'] == 'writInput')
            self.assertTrue(return_query1['iLink'] == '1')
            self.assertTrue(return_query1['sLink'] == '1')
            self.assertTrue(return_query1['blanks'] == 'a__d')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(return_query2 is not None)
            self.assertTrue(return_query2['Prompt'] == 'question 1')
            self.assertTrue(return_query2['Choices'] == 'abcd')
            self.assertTrue(return_query2['Solution'] == 'a')
            self.assertTrue(return_query2['zone'] == 'Nonfiction')
            self.assertTrue(return_query2['branch'] == 'Clareview2')
            self.assertTrue(return_query2['qType'] == 'writInput')
            self.assertTrue(return_query2['iLink'] == '1')
            self.assertTrue(return_query2['sLink'] == '1')
            self.assertTrue(return_query2['blanks'] == 'a__d')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)


    def test_delete_question(self):
        """Tests deleting a question from the db"""
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

            # After the constraints for zone and branch
            # are satisfied, create the question
            prompt = 'question 1'
            choices = 'abcd'
            solution = 'a'
            zone = 'Nonfiction'
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
            self.assertTrue(return_query['zone'] == 'Nonfiction')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['qType'] == 'writInput')
            self.assertTrue(return_query['iLink'] == '1')
            self.assertTrue(return_query['sLink'] == '1')
            self.assertTrue(return_query['blanks'] == 'a__d')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)

            # Delete the question
            delete_url = '/deleteQuestion/' + str(return_query['id'])

            delete_response = self.client.delete(
                delete_url,
                content_type = 'application/json'
            )
            data = json.loads(delete_response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully deleted question.')
            self.assertTrue(delete_response.content_type == 'application/json')
            self.assertEqual(delete_response.status_code, 200)            

            # Verify that there is no such question
            url = '/getQuestion/' + zone + '/' \
                  + branch

            get_response = self.client.get(
                url,
                content_type = 'application/json'
            )
            data = json.loads(get_response.data.decode())

            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'No data')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 404)

    def test_update_question(self):
        """ Tests updating a question from the db """
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

            # After the constraints for zone and branch
            # are satisfied, create the question
            prompt = 'question 1'
            choices = 'abcd'
            solution = 'a'
            zone = 'Nonfiction'
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
            self.assertTrue(return_query['zone'] == 'Nonfiction')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['qType'] == 'writInput')
            self.assertTrue(return_query['iLink'] == '1')
            self.assertTrue(return_query['sLink'] == '1')
            self.assertTrue(return_query['blanks'] == 'a__d')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)
			
            # Editing the question for update
            prompt = 'question 1 - changed'
            choices = 'abcd - changed'
            solution = 'a - changed'
            zone = 'Nonfiction'
            branch = 'Clareview'
            qtype = 'writInput - changed'
            ilink = '1 - changed'
            slink = '1 - changed'
            blanks = 'a__d - changed'

            # Update question
            url = '/updateQuestion/' + str(return_query['id']) + '/' \
                  + prompt + '/' \
                  + choices + '/' \
                  + solution + '/' \
                  + zone + '/' \
                  + branch + '/' \
                  + qtype + '/' \
                  + ilink + '/' \
                  + slink + '/' \
                  + blanks

            update_response = self.client.post(
                url,
                content_type = 'application/json'
            )
            data = json.loads(update_response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully updated question.')
            self.assertTrue(update_response.content_type == 'application/json')
            self.assertEqual(update_response.status_code, 201)

            # Get the question that was just updated
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
            self.assertTrue(return_query['Prompt'] == 'question 1 - changed')
            self.assertTrue(return_query['Choices'] == 'abcd - changed')
            self.assertTrue(return_query['Solution'] == 'a - changed')
            self.assertTrue(return_query['zone'] == 'Nonfiction')
            self.assertTrue(return_query['branch'] == 'Clareview')
            self.assertTrue(return_query['qType'] == 'writInput - changed')
            self.assertTrue(return_query['iLink'] == '1 - changed')
            self.assertTrue(return_query['sLink'] == '1 - changed')
            self.assertTrue(return_query['blanks'] == 'a__d - changed')
            self.assertTrue(get_response.content_type == 'application/json')
            self.assertEqual(get_response.status_code, 200)
