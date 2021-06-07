from flask import request, jsonify
from src import app
from src.models.assistance import assistanceModel
ASSISTANCEMODEL = assistanceModel()

def convert():
    found = ASSISTANCEMODEL.listAssistance()
    arr = []
    for element in found:
        arr.append({
            'id' : element[0],
            'date' : element[1],
            'cut' : element[2], 
            'time_start' : element[3],
            'identification' : element[4],
            'student' : element[5],
            'surname' : element[6],
            'semester' : element[7],
            'assistance': element[8]
        })
    return arr


@app.route('/Assistances', methods=['GET', 'POST'])
def indexAssistance():
    if request.method == 'GET':
        return jsonify({'Assistance': convert()})
    data = {
        'student': request.json['student_id'],
        'session': request.json['session_id'],
        'assistance' : request.json['assistance']
    }
    ASSISTANCEMODEL.createAssistance(data)
    return jsonify({'Assistance': convert()})

@app.route('/Assistances/<assistance>', methods=['PUT','DELETE'])
def editAssistance(assistance):
    if request.method == 'DELETE':
        ASSISTANCEMODEL.removeAssistance(assistance)
        return jsonify({'Assistance': convert()})
    data = {
        'id': assistance,
        'student': request.json['student_id'],
        'session': request.json['session_id'],
        'assistance' : request.json['assistance']
    }
    ASSISTANCEMODEL.editAssistance(data)
    return jsonify({'Assistance': convert()})