from flask import request, jsonify
from src import app
from src.models.notes import notesModel
NOTESMODEL=notesModel()

def convert():
    found = NOTESMODEL.listNotesStudents()
    arr = []
    for element in found:
        arr.append({
            'id_nota' : element[0],
            'CC' : element[1],
            'name' : element[2],
            'surname' : element[3],
            'semester' : element[4],
            'note' : element[5],
            'commentary' : element[6],
            'partial_activity_id' : element[7]
        })
    return arr

@app.route('/Notes', methods=['GET','POST'])
def indexNotes():
    if request.method == 'GET':
        return jsonify({'Notes': convert()})
    data = {
        'student': request.json['student_id'],
        'note': request.json['note'],
        'commentary': request.json['commentary'],
        'activity': request.json['activity_id']
    }
    NOTESMODEL.createNote(data)
    return jsonify({'Notes': convert()})

@app.route('/Notes/<idNote>', methods=['PUT','DELETE'])
def editNote(idNote):
    if request.method == 'DELETE':
        NOTESMODEL.removeNote(idNote)
        return jsonify({'Notes': convert()})
    data = {
        'id' : idNote,
        'student_id': request.json['student_id'],
        'activity_id': request.json['activity_id'],
        'note' : request.json['note'],
        'commentary' : request.json['commentary']
    }
    NOTESMODEL.editNote(data)
    return jsonify({'Notes': convert()})

