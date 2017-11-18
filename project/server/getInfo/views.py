# project/server/getInfo

from flask import Blueprint, request, make_response, jsonify
from flask import json

from project.server import db
from project.server.models import Question, Zone, Branch

import collections

info_blueprint = Blueprint('getInfo', __name__)

@info_blueprint.route('/createQuestion/<prompt>/<choices>/<solution>/' + \
                      '<zone>/<branch>/<qtype>/<ilink>/<slink>/<blanks>', methods = ['POST'])
def createQuestion(prompt, choices, solution, zone, branch, qtype, ilink, slink, blanks):
    try:
        question = Question(
            Prompt=prompt,
            Choices=choices,
            Solution=solution,
            zone=zone,
            branch=branch,
            qType=qtype,
            iLink=ilink,
            sLink=slink,
            blanks=blanks
        )
        db.session.add(question)
        db.session.commit()
        responseObject = {
            'status' : 'success',
            'message': 'Successfully created question.'
        }
        return make_response(jsonify(responseObject)), 201
    except Exception as e:
        responseObject = {
            'status': 'fail',
            'message': 'Some error occured.'
        }
        print(e)
        return make_response(jsonify(responseObject)), 401

@info_blueprint.route('/getQuestion/<zone>/<branch>', methods = ['GET'])
def getQuestion(zone, branch):
    try:
        connection = db.engine.raw_connection()
        cur = connection.cursor()

        stmt = "SELECT Prompt, Choices, Solution, zone, branch, qType, iLink, sLink, id, blanks \
        FROM questions \
        WHERE zone = %(zone)s AND branch = %(branch)s"

        cur.execute(stmt, {'zone': zone, 'branch': branch})
        rows = cur.fetchall()

        return_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['Prompt'] = row[0]
            d['Choices'] = row[1]
            d['Solution'] = row[2]
            d['zone'] = row[3]
            d['branch'] = row[4]
            d['qType'] = row[5]
            d['iLink'] = row[6]
            d['sLink'] = row[7]
            d['id'] = row[8]
            d['blanks'] = row[9]
            return_list.append(d)
            
        responseObject = {
            'status' : 'success',
            'data': return_list
        }
        connection.close()
        return make_response(jsonify(responseObject)), 200
    except Exception as e:
        responseObject = {
            'status' : 'fail',
            'message' : 'Database connection failed'
        }
        connection.close()
        return make_response(jsonify(responseObject)), 500
    
@info_blueprint.route('/createZone/<new_beaconID>/<new_zone>/<new_branch>/' + \
                      '<new_area>/<new_color>', methods = ['POST'])
def createZone(new_beaconID, new_zone, new_branch, new_area, new_color):
    try:
        zone = Zone(
            beaconID=new_beaconID,
            zone=new_zone,
            branch=new_branch,
            area=new_area,
            color=new_color
        )
        db.session.add(zone)
        db.session.commit()
        responseObject = {
            'status' : 'success',
            'message' : 'Successfully created zone.'
        }
        return make_response(jsonify(responseObject)), 201
    except Exception as e:
        responseObject = {
            'status' : 'fail',
            'message': 'Some error occured.'
        }
        print(e)
        return make_response(jsonify(responseObject)), 401
        
@info_blueprint.route('/getZone/<branch>', methods = ['GET'])
def getZones(branch):
    try:
        connection = db.engine.raw_connection()
        cur = connection.cursor()

        stmt = "SELECT beaconID, zone, branch, area, color \
        FROM zone\
        WHERE branch = %(branch)s"

        cur.execute(stmt, {'branch': branch})
        rows = cur.fetchall()

        return_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['beaconID'] = row[0]
            d['zone'] = row[1]
            d['branch'] = row[2]
            d['area'] = row[3]
            d['color'] = row[4]
            return_list.append(d)

        responseObject = {
            'status' : 'success',
            'data' : return_list
        }
        connection.close()
        return make_response(jsonify(responseObject)), 200
    except Exception as e:
        responseObject = {
            'status' : 'fail',
            'message' : 'Database connection failed.'
        }
        print(e)
        connection.close()
        return make_response(jsonify(responseObject)), 500
        
@info_blueprint.route('/createBranch/<new_branch>/<new_iLink>', methods = ['POST'])
def createBranch(new_branch, new_iLink):
    try:
        branch = Branch(
            branch=new_branch,
            iLink=new_iLink
        )

        db.session.add(branch)
        db.session.commit()

        responseObject = {
            'status' : 'success',
            'message' : 'Successfully created branch.'
        }
        return make_response(jsonify(responseObject)), 201
    except Exception as e:
        responseObject = {
            'status' : 'fail',
            'message' : 'Some error occured.'
        }
        print(e)
        return make_response(jsonify(responseObject)), 401

@info_blueprint.route('/getBranch', methods = ['GET'])
def getBranch():
    try:
        connection = db.engine.raw_connection()
        cur = connection.cursor()

        stmt = "SELECT branch, iLink \
        FROM branch"

        cur.execute(stmt)
        rows = cur.fetchall()

        return_list = []
        for row in rows:
            d = collections.OrderedDict()
            d['branch'] = row[0]
            d['iLink'] = row[1]
            return_list.append(d)

        responseObject = {
            'status' : 'success',
            'data' : return_list
        }
        connection.close()
        return make_response(jsonify(responseObject)), 200
    except Exception as e:
        responseObject = {
            'status' : 'fail',
            'message' : 'Database connection failed.'
        }
        print(e)
        connection.close()
        return make_response(jsonify(responseObject)), 500
