# PROJECT20/server/models.py

import datetime
import jwt

from project.server import app, db, bcrypt

class User(db.Model):
    """ 
    User Model for storing user related details
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
                }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
                
class Branch(db.Model):
    """
    Branch Model
    """
    __tablename__ = 'branch'

    branch = db.Column(db.String(30), primary_key=True)
    iLink = db.Column(db.String(255), nullable=True)
    
    def __init__(self, branch, iLink):
        self.branch = branch
        self.iLink = iLink

        
class Zone(db.Model):
    """
    Zone Model for storing zones
    """
    __tablename__ = 'zone'
    beaconID = db.Column(db.String(50), nullable=True)
    zone = db.Column(db.String(30), primary_key=True)
    branch = db.Column(db.String(30), primary_key=True)
    area = db.Column(db.String(255), nullable=True)
    color = db.Column(db.String(255), nullable=True)

    __table_args__ = (db.ForeignKeyConstraint([branch],
                                              [Branch.branch]),
                      {})
    
    def __init__(self, beaconID, zone, branch, area, color):
        self.beaconID = beaconID
        self.zone = zone
        self.branch = branch
        self.area = area
        self.color = color

class Question(db.Model):
    """
    Question Model for storing questions
    """
    __tablename__ = 'questions'

    Prompt = db.Column(db.String(255), nullable=True)
    Choices = db.Column(db.String(255), nullable=True)
    Solution = db.Column(db.String(255), nullable=True)
    zone = db.Column(db.String(30), nullable=True)
    branch = db.Column(db.String(30), nullable=True)
    qType = db.Column(db.String(255), nullable=True)
    iLink = db.Column(db.String(255), nullable=True)
    sLink = db.Column(db.String(255), nullable=True)
    blanks = db.Column(db.String(255), nullable=True)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    __table_args__ = (db.ForeignKeyConstraint([branch, zone],
                                              [Zone.branch, Zone.zone]),
                      {})

    def __init__(self, Prompt, Choices, Solution, zone, branch,
                 qType, iLink, sLink, blanks):
        self.Prompt = Prompt
        self.Choices = Choices
        self.Solution = Solution
        self.zone = zone
        self.branch = branch
        self.qType = qType
        self.iLink = iLink
        self.sLink = sLink
        self.blanks = blanks
