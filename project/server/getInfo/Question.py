# project/server/getInfo

from flask import Blueprint, make_response, jsonify

from project.server import db
from project.server.models import Question

import collections

question_blueprint = Blueprint('question', __name__)

@question_blueprint.route('/createQuestion/<prompt>/<choices>/<solution>/' + \
                      '<zone>/<branch>/<qtype>/<path:ilink>/<slink>/<blanks>', methods = ['POST'])
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
        # Insert the Question
        db.session.add(question)
        db.session.commit()

        responseObject = {
            'status' : 'success',
            'message': 'Successfully created question.'
        }
        return make_response(jsonify(responseObject)), 201
    except Exception as e:
        print(e)
        responseObject = {
            'status': 'fail',
            'message': 'Some error occured.'
        }
        print(e)
        return make_response(jsonify(responseObject)), 401

@question_blueprint.route('/deleteQuestion/<id>', methods = ['DELETE'])
def deleteQuestion(id):
    try:
        connection = db.engine.raw_connection()
        cur = connection.cursor()

        stmt = "DELETE FROM questions \
        WHERE id = '%s'" %(id)

        cur.execute(stmt)
        connection.commit()

        responseObject = {
            'status': 'success',
            'message': 'Successfully deleted question.'
        }
        return make_response(jsonify(responseObject)), 200
    except Exception as e:
        responseObject = {
            'status': 'fail',
            'message': 'Some error occured.'
        }
        print(e)
        return make_response(jsonify(responseObject)), 404


@question_blueprint.route('/getQuestion/<zone>/<branch>', methods = ['GET'])
def getQuestion(zone, branch):
    try:
        connection = db.engine.raw_connection()
        cur = connection.cursor()

        stmt = "SELECT Prompt, Choices, Solution, zone, branch, qType, iLink, sLink, id, blanks \
        FROM questions \
        WHERE zone = %(zone)s AND branch = %(branch)s"

        cur.execute(stmt, {'zone': zone, 'branch': branch})
        rows = cur.fetchall()

        # Parse the output into a
        # list of dictionaries
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
        if not return_list:
            responseObject = {
                'status' : 'success',
                'message' : 'No data'
            }
            connection.close()
            return make_response(jsonify(responseObject)), 404
        else:
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

@question_blueprint.route('/getAllQuestions/', methods = ['GET'])
def getAllQuestions():
    try:
        connection = db.engine.raw_connection()
        cur = connection.cursor()

        stmt = "SELECT Prompt, Choices, Solution, zone, branch, qType, iLink, sLink, id, blanks \
        FROM questions"

        cur.execute(stmt)
        rows = cur.fetchall()

        # Parse the output into a
        # list of dictionaries
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
        if not return_list:
            responseObject = {
                'status' : 'success',
                'message' : 'No data'
            }
            connection.close()
            return make_response(jsonify(responseObject)), 404
        else:
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


@question_blueprint.route('/updateQuestion/<id>/<prompt>/<choices>/<solution>/' + \
                      '<zone>/<branch>/<qtype>/<path:ilink>/<slink>/<blanks>', methods = ['POST'])
def updateQuestion(id, prompt, choices, solution, zone, branch, qtype, ilink, slink, blanks):
    try:
        question = Question.query.get(id)
        question.Prompt   = prompt
        question.Choices  = choices
        question.Solution = solution
        question.zone     = zone
        question.branch   = branch
        question.qType    = qtype
        question.iLink    = ilink
        question.sLink    = slink
        question.blanks   = blanks

        db.session.commit()
        responseObject = {
            'status' : 'success',
            'message': 'Successfully updated question.'
        }
        return make_response(jsonify(responseObject)), 201
    except Exception as e:
        print(e)
        responseObject = {
            'status' : 'fail',
            'message' : 'Database connection failed'
        }
        return make_response(jsonify(responseObject)), 500
