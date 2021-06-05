from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.students import studentModel
from src.models.periods import periodsModel
STUDENTMODEL = studentModel()
PERIODMODEL = periodsModel()
@app.route('/Students', methods=['GET','POST'])
def indexStudents():
    if request.method == 'GET':
        if not 'period' in Global.session:
            Global.session['period'] = 1
        return render_template('students/indexStudents.html', periods = PERIODMODEL.listPeriods(), students=STUDENTMODEL.listStudents(Global.session['period']), pd = int(Global.session['period']))
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('indexStudents'))

@app.route('/Create/Student', methods=['GET','POST'])
def createStudent():
    if request.method == 'GET':
        return render_template('students/createStudent.html')
    data = {
        'identification' : request.form.get('identification'),
        'name' : request.form.get('name'),
        'surname' : request.form.get('surname'),
        'phone_number' : request.form.get('phone_number'),
        'email' : request.form.get('email'),
        'semester' : request.form.get('semester'),
        'period_id' : Global.session['period']
    }
    STUDENTMODEL.createStudent(data)
    return redirect(url_for('indexStudents'))

@app.route('/Edit/Student/<idStudent>', methods=['GET','POST'])
def editStudent(idStudent):
    if request.method == 'GET': 
        return render_template('students/EditStudent.html', student = STUDENTMODEL.findStudent(idStudent), periods = PERIODMODEL.listPeriods())
    data = {
        'identification' : request.form.get('identification'),
        'name' : request.form.get('name'),
        'surname' : request.form.get('surname'),
        'phone_number' : request.form.get('phone_number'),
        'email' : request.form.get('email'),
        'semester' : request.form.get('semester'),
        'period_id' : Global.session['period'],
        'id': idStudent
    }
    STUDENTMODEL.editStudent(data)
    return redirect(url_for('indexStudents'))

@app.route('/Remove/Student/<idStudent>')
def removeStudent(idStudent):
    STUDENTMODEL.removeStudent(idStudent)
    return redirect(url_for('indexStudents'))



