from flask import request, jsonify
from src import app
from src.models.students import studentModel
STUDENTMODEL = studentModel()

def convert():
    found = STUDENTMODEL.listStudents()
    arr = []
    for element in found:
        arr.append({
            'id' : element[0],
            'identification' : element[1],
            'name' : element[2],
            'surname' : element[3],
            'phone_number' : element[4],
            'email' : element[5],
            'semester' : element[6],
            'period_id' : element[7]
        })
    return arr

@app.route('/Students', methods=['GET','POST'])
def indexStudents():
    if request.method == 'GET':
        return jsonify({'Students': convert()})
    data = {
        'identification' : request.json['identification'],
        'name' : request.json['name'],
        'surname' : request.json['surname'],
        'phone_number' : request.json['phone_number'],
        'email' : request.json['email'],
        'semester' : request.json['semester'],
        'period_id' : request.json['period_id']
    }
    STUDENTMODEL.createStudent(data)
    return jsonify({'Students': convert()})

@app.route('/Students/<idStudent>', methods=['PUT','DELETE'])
def editStudent(idStudent):
    if request.method == 'DELETE': 
        STUDENTMODEL.removeStudent(idStudent)
        return jsonify({'Students': convert()})
    data = {
        'identification' : request.json['identification'],
        'name' : request.json['name'],
        'surname' : request.json['surname'],
        'phone_number' : request.json['phone_number'],
        'email' : request.json['email'],
        'semester' : request.json['semester'],
        'period_id' :request.json['period_id'],
        'id': idStudent
    }
    STUDENTMODEL.editStudent(data)
    return jsonify({'Students': convert()})


