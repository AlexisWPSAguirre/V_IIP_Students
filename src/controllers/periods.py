from flask import request, jsonify
from src import app
from src.models.periods import periodsModel
PERIODMODEL = periodsModel()

""" Mostrar en un diccionario los arreglos """
def convert():
    found = PERIODMODEL.listPeriods()
    arr = []
    for element in found:
        data = {
            'id' : element[0],
            'date' : element[1],
            'period' : element[2],
        }
        arr.append(data)
    return arr

@app.route("/periods", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return jsonify({'periods': convert()})
    data = {
        'date' : request.json['date'],
        'period' : request.json['period']
    }
    print(data)
    PERIODMODEL.createPeriod(data)
    return jsonify({'periods': convert()})


@app.route("/periods/<idPeriod>", methods=['DELETE','PUT'])
def editPeriod(idPeriod):
    if request.method == 'DELETE':
        PERIODMODEL.removePeriod(idPeriod)
        return jsonify({'periods': convert()})
    data = {
        'id' : idPeriod,
        'date' : request.json['date'],
        'period' : request.json['period']
    }
    PERIODMODEL.editPeriod(data)
    return jsonify({'periods': convert()})












    
    








