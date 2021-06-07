from flask import request, jsonify
from src import app
from src.models.academicSpaces import academicModel
ACADEMICMODEL = academicModel()


def convert():
    found = ACADEMICMODEL.listAcademic()
    arr = []
    for element in found:
        arr.append({
            'id' : element[0],
            'period_id' : element[1],
            'name' : element[2],
            'semester' : element[3]
        })
    return arr

@app.route('/AcademicSpaces', methods=['GET','POST'])
def indexAcademicSpace():
    if request.method == 'GET':
        return jsonify({'Academic Spaces': convert()})
    data = {
        'name' : request.json['name'],
        'semester' : request.json['semester'],
        'period_id': request.json['period_id']
    }
    ACADEMICMODEL.createAcademicSpace(data)
    return jsonify({'Academic Spaces': convert()})


@app.route('/AcademicSpaces/<idSpace>', methods=['PUT','DELETE'])
def editAcademicSpace(idSpace):
    if request.method == 'DELETE':
        ACADEMICMODEL.removeAcademicSpace(idSpace)
        return jsonify({'Academic Spaces': convert()})
    data = {
        'id' : idSpace,
        'name' : request.json['name'],
        'semester' : request.json['semester'],
        'period_id': request.json['period_id']
    }
    ACADEMICMODEL.editAcademicSpace(data)
    return jsonify({'Academic Spaces': convert()})