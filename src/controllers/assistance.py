from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.notes import notesModel
from src.models.students import studentModel
from src.models.periods import periodsModel
from src.models.assistance import assistanceModel
NOTESMODEL=notesModel()
STUDENTMODEL = studentModel()
PERIODMODEL = periodsModel()
ASSISTANCEMODEL = assistanceModel()

@app.route('/Assistance/Student/<idSession>')
def indexAssistance(idSession):
    Global.session['session'] = idSession
    return render_template('assistance/indexAssistance.html', students = ASSISTANCEMODEL.listAssistance(idSession) )

@app.route('/Create/Assistance/Student/<idStudent>', methods=['GET','POST'])
def createAssistance(idStudent=None):
    if request.method == 'GET':
        return render_template('assistance/createAssistance.html', selected = STUDENTMODEL.findStudent(idStudent))
    
    data = {
        'student': idStudent,
        'session':Global.session['session'],
        'assistance' : request.form.get('assistance')
    }
    ASSISTANCEMODEL.createAssistance(data)
    return redirect(url_for('indexAssistance', idSession = Global.session['session']))

@app.route('/Select/Student/Assistance', methods=['GET','POST'])
def selectStudentAssistance():
    if request.method == 'GET':
        return render_template('assistance/selectStudentAssistance.html', periods = PERIODMODEL.listPeriods(), students=STUDENTMODEL.listStudents(Global.session['period']), pd = int(Global.session['period']))
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('selectStudentAssistance'))

@app.route('/Edit/Assistance/<assistance>', methods=['GET','POST'])
def editAssistance(assistance):
    if request.method == 'GET':
        return render_template('assistance/editAssistance.html', assistance = ASSISTANCEMODEL.findAssistance(assistance))
    
    data = {
        'id': assistance,
        'assistance' : request.form.get('assistance')
    }
    ASSISTANCEMODEL.editAssistance(data)
    return redirect(url_for('indexAssistance', idSession = Global.session['session']))

@app.route('/Remove/Assistance/<assistance>')
def removeAssistance(assistance):
    ASSISTANCEMODEL.removeAssistance(assistance)
    return redirect(url_for('indexAssistance', idSession = Global.session['session']))