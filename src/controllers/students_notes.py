from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.notes import notesModel
from src.models.students import studentModel
from src.models.periods import periodsModel
NOTESMODEL=notesModel()
STUDENTMODEL = studentModel()
PERIODMODEL = periodsModel()

@app.route('/Notes/Activities/Partials/<idActivity>')
def indexNotes(idActivity):
    Global.session['activity'] = idActivity
    return render_template('notes/indexNotes.html', students = NOTESMODEL.listNotesStudents(idActivity))

@app.route('/Create/Notes/Activities/Partials', methods=['GET','POST'])
@app.route('/Create/Notes/Activities/Partials/<selected>', methods=['GET','POST'])
def createNote(selected=None):
    if request.method == 'GET':
        return render_template('notes/createNote.html', selected = STUDENTMODEL.findStudent(selected))
    data = {
        'activity':Global.session['activity'],
        'student':selected,
        'note': request.form.get('note'),
        'commentary': request.form.get('commentary'),
    }
    NOTESMODEL.createNote(data)
    return redirect(url_for('indexNotes', idActivity = Global.session['activity']))

@app.route('/Select/Student', methods=['GET','POST'])
def selectStudent():
    if request.method == 'GET':
        return render_template('notes/selectStudent.html', periods = PERIODMODEL.listPeriods(), students=STUDENTMODEL.listStudents(Global.session['period']),pd = int(Global.session['period']))
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('selectStudent'))

@app.route('/Edit/Notes/Activities/Partials/<idNote>', methods=['GET','POST'])
def editNote(idNote):
    if request.method == 'GET':
        return render_template('notes/editNote.html', editNote = NOTESMODEL.findNote(idNote))
    data = {
        'id' : idNote,
        'note' : request.form.get('note'),
        'commentary' : request.form.get('commentary')
    }
    NOTESMODEL.editNote(data)
    return redirect(url_for('indexNotes', idActivity = Global.session['activity']))

@app.route('/Remove/Note/Activity/Partial/<idNote>')
def removeNote(idNote):
    NOTESMODEL.removeNote(idNote)
    return redirect(url_for('indexNotes', idActivity = Global.session['activity']))
