from flask import request, jsonify
from src import app
from src.models.activitiesParcials import activitiesModel
ACTIVITIESMODEL = activitiesModel() 

def convert():
    found = ACTIVITIESMODEL.listActivities()
    arr = []
    for element in found:
        arr.append({
            'id' : element[0],
            'space_id' : element[1],
            'date' : element[2],
            'cut' : element[3],
            'name' : element[4],
            'porcentage_in_cut' : element[5],
        })
    return arr

@app.route('/Activities-Partials', methods=['GET','POST'])
def indexActivities():
    if request.method == 'GET':
        return jsonify({'Activities-Partials': convert()})
    data = {
        'name': request.json['name'],
        'date': request.json['date'],
        'cut': request.json['cut'],
        'porcentage': request.json['porcentage'],
        'academic_space' : request.json['space_id'],
    }
    ACTIVITIESMODEL.createActivity(data)
    return jsonify({'Activities-Partials': convert()})

@app.route('/Activities-Partials/<idActivity>', methods=['PUT','DELETE'])
def editActivitiesPartials(idActivity):
    if request.method == 'DELETE':
        ACTIVITIESMODEL.removeActivity(idActivity)
        return jsonify({'Activities-Partials': convert()})
    data = {
        'id': idActivity,
        'name': request.json['name'],
        'date': request.json['date'],
        'cut': request.json['cut'],
        'porcentage': request.json['porcentage'],
        'academic_space' : request.json['space_id'],
    }
    ACTIVITIESMODEL.editActivity(data)
    return jsonify({'Activities-Partials': convert()})
