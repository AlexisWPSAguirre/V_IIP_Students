from flask import request, jsonify
from src import app
from src.models.session import sessionModel
SESSIONMODEL = sessionModel()

def convert():
    found = SESSIONMODEL.listSession()
    arr = []
    for element in found:
        arr.append({
            'id' : element[0],
            'academic_space_id' : element[1],
            'date' : element[2],
            'cut' : element[3],
            'time_start' : element[4],
            'time_end' : element[5],
        })
    return arr

@app.route('/Sessions', methods=['GET','POST'])
def indexSession():
    if request.method == 'GET':
        return jsonify({'Sessions': convert()})
    data = {
        'space' : request.json['space'],
        'date' : request.json['date'],
        'cut' : request.json['cut'],
        'start' : request.json['time_start'],
        'end' : request.json['time_end']
    }
    SESSIONMODEL.createSession(data)
    return jsonify({'Sessions': convert()})

@app.route('/Sessions/<idSession>', methods=['PUT','DELETE'])
def editSession(idSession):
    if request.method == 'DELETE':
        SESSIONMODEL.removeSession(idSession)
        return jsonify({'Sessions': convert()})
    data = {
        'id': idSession,
        'space' : request.json['space'],
        'date' : request.json['date'],
        'cut' : request.json['cut'],
        'start' : request.json['time_start'],
        'end' : request.json['time_end']
    }
    SESSIONMODEL.editSession(data)
    return jsonify({'Sessions': convert()})
