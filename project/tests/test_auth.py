# project/tests

import unittest
import json
import time

from project.server import db
from project.server.models import User, BlacklistToken
from project.tests.base import BaseTestCase

def register_user(self, email, password):
    return self.client.post(
        '/auth/register',
        data = json.dumps(dict(
            email = email,
            password = password
        )),
        content_type = 'application/json',
    )

def login_user(self, email, password):
    return self.client.post(
        '/auth/login',
        data = json.dumps(dict(
            email = email,
            password = password
        )),
        content_type = 'application/json',
    )

class TestAuthBlueprint(BaseTestCase):
    
    def test_registration(self):
        """ Test for user registration """
        with self.client:
            response = register_user(self, 'test@gmail.com', 'test123')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(data['auth_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_registered_with_already_registered_user(self):
        """ Test registration with already registered email"""
        user = User(
            email = 'test@gmail.com',
            password = 'test'
        )
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = register_user(self, 'test@gmail.com', 'test123')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'User already exists. Please Log in.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 202)

    def test_registered_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            # Registering a user
            resp_register = register_user(self, 'test@gmail.com', 'test123')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.'
            )
            self.assertTrue(data_register['auth_token'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            
            # Logging in with the created user
            response = login_user(self, 'test@gmail.com', 'test123')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged in.')
            self.assertTrue(data['auth_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        """ Test for non-existant and invalid login """
        with self.client:
            # Logging in with a non existant user
            response = login_user(self, 'test@gmail.com', 'test123')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'The username and password combination do not match our records.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)
            
            # Registering a user
            resp_register = register_user(self, 'test@gmail.com', 'test123')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.'
            )
            self.assertTrue(data_register['auth_token'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            
            # Logging in with a wrong password
            resp_invalid = login_user(self, 'test@gmail.com', 'test12')
            data_invalid = json.loads(resp_invalid.data.decode())
            self.assertTrue(data_invalid['status'] == 'fail')
            self.assertTrue(
                data_invalid['message'] == 'The username and password combination do not match our records.')
            self.assertTrue(resp_invalid.content_type == 'application/json')
            self.assertEqual(resp_invalid.status_code, 404)

            # Logging in with a wrong username
            resp_invalid = login_user(self, 'tes@gmail.com', 'test123')
            data_invalid = json.loads(resp_invalid.data.decode())
            self.assertTrue(data_invalid['status'] == 'fail')
            self.assertTrue(
                data_invalid['message'] == 'The username and password combination do not match our records.')
            self.assertTrue(resp_invalid.content_type == 'application/json')
            self.assertEqual(resp_invalid.status_code, 404)

            
    def test_user_status(self):
        """ Test for user status """
        with self.client:
            resp_register = register_user(self, 'test@gmail.com', 'test123')
            response = self.client.get(
                '/auth/status',
                headers = dict(
                    Authorization = 'Bearer ' + json.loads(
                        resp_register.data.decode()
                    )['auth_token']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(data['data']['email'] == 'test@gmail.com')
            self.assertTrue(data['data']['admin'] is 'true' or 'false')
            self.assertEqual(response.status_code, 200)

    def test_valid_logout(self):
        """ Test for logout before token expires """
        with self.client:
            # Registering a user
            resp_register = register_user(self, 'test@gmail.com', 'test123')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.')
            self.assertTrue(data_register['auth_token'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            
            # Logging in with the created user
            resp_login = login_user(self, 'test@gmail.com', 'test123')
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login['status'] == 'success')
            self.assertTrue(data_login['message'] == 'Successfully logged in.')
            self.assertTrue(data_login['auth_token'])
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            
            # Checking for a valid token
            response = self.client.post(
                '/auth/logout',
                headers = dict(
                    Authorization ='Bearer ' + json.loads(
                        resp_login.data.decode()
                    )['auth_token']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged out.')
            self.assertEqual(response.status_code, 200)

    @unittest.skip("Skipping because of token timeout length")
    def test_invalid_logout(self):
        """
        Testing logout after the token expires
        """
        with self.client:
            # Registering a user
            resp_register = register_user(self, 'test@gmail.com', 'test123')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.')
            self.assertTrue(data_register['auth_token'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            
            # Logging in with the created user
            resp_login = login_user(self, 'test@gmail.com', 'test123')
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login['status'] == 'success')
            self.assertTrue(data_login['message'] == 'Successfully logged in.')
            self.assertTrue(data_login['auth_token'])
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            
            # Logging out with an expired token
            time.sleep(6) # Dependent on token logout time
            response = self.client.post(
                '/auth/logout',
                headers = dict(
                    Authorization = 'Bearer ' + json.loads(
                        resp_login.data.decode()
                    )['auth_token']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'Signature expired. Please log in again.')
            self.assertEqual(response.status_code, 401)

    def test_valid_blacklisted_token_logout(self):
        """ Test for logout after a valid token gets blacklisted """
        with self.client:
            # Registering a user
            resp_register = register_user(self, 'test@gmail.com', 'test123')
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            self.assertTrue(
                data_register['message'] == 'Successfully registered.')
            self.assertTrue(data_register['auth_token'])
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            
            # Logging in with the created user
            resp_login = login_user(self, 'test@gmail.com', 'test123')
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login['status'] == 'success')
            self.assertTrue(data_login['message'] == 'Successfully logged in.')
            self.assertTrue(data_login['auth_token'])
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            
            # Blacklisting the token
            blacklist_token = BlacklistToken(
                token=json.loads(resp_login.data.decode())['auth_token'])
            db.session.add(blacklist_token)
            db.session.commit()

            # Logging out with a blacklisted token
            response = self.client.post(
                '/auth/logout',
                headers = dict(
                    Authorization = 'Bearer ' + json.loads(
                        resp_login.data.decode()
                    )['auth_token']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Token blacklisted. Please log in again.')
            self.assertEqual(response.status_code, 401)

    def test_valid_blacklisted_token_user(self):
        """ Test for user status with a blacklisted valid token """
        with self.client:
            # Registering a user
            resp_register = register_user(self, 'test123@gmail.com', 'test123')

            # Blacklisting the token
            blacklist_token = BlacklistToken(
                token=json.loads(resp_register.data.decode())['auth_token'])
            db.session.add(blacklist_token)
            db.session.commit()

            # Checking user status
            response = self.client.get(
                '/auth/status',
                headers = dict(
                    Authorization = 'Bearer ' + json.loads(
                        resp_register.data.decode()
                    )['auth_token']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Token blacklisted. Please log in again.')
            self.assertEqual(response.status_code, 401)
                            
    def test_user_status_malformed_bearer_token(self):
        """ Test for user status with malformed bearer token """
        with self.client:
            # Registering a user
            resp_register = register_user(self, 'test@gmail.com', 'test123')

            # Malformed token
            response = self.client.get(
                '/auth/status',
                headers = dict(
                    Authorization = 'Bearer' + json.loads(  # Bearer doesn't have a space
                        resp_register.data.decode()
                    )['auth_token']
                )
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Bearer token malformed.')
            self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
