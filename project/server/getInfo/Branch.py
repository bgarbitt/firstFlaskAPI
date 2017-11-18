# project/server/getInfo

from flask import Blueprint, make_response, jsonify

from project.server import db
from project.server.models import Branch

import collections

branch_blueprint = Blueprint('branch', __name__)

@branch_blueprint.route('/createBranch/<new_branch>/<new_iLink>', methods = ['POST'])
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

@branch_blueprint.route('/getBranch', methods = ['GET'])
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
