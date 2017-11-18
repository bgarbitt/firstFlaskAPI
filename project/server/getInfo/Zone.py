# project/server/getInfo

from flask import Blueprint, make_response, jsonify

from project.server import db
from project.server.models import Zone

import collections

zone_blueprint = Blueprint('zone', __name__)

@zone_blueprint.route('/createZone/<new_beaconID>/<new_zone>/<new_branch>/' + \
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

        # Insert the zone
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
        
@zone_blueprint.route('/getZone/<branch>', methods = ['GET'])
def getZones(branch):
    try:
        connection = db.engine.raw_connection()
        cur = connection.cursor()

        stmt = "SELECT beaconID, zone, branch, area, color \
        FROM zone\
        WHERE branch = %(branch)s"

        cur.execute(stmt, {'branch': branch})
        rows = cur.fetchall()

        # Parse the output into a
        # list of dictionaries
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
