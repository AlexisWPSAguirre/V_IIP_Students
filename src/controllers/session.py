from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.session import sessionModel
from src.models.students import studentModel
from src.models.periods import periodsModel
from src.models.academicSpaces import academicModel
SESSIONMODEL = sessionModel()
STUDENTMODEL = studentModel()
PERIODMODEL = periodsModel()
ACADEMICMODEL = academicModel()

@app.route('/Session', methods=['GET','POST'])
def indexSession():
    if request.method == 'GET':
        return render_template('sessions/indexSession.html', academicSpaces= ACADEMICMODEL.listAcademic(Global.session['period']), sessions =  SESSIONMODEL.listSession(Global.session['space']),  pd = int(Global.session['space']))
    Global.session['space'] = request.form.get('space')
    return redirect(url_for('indexSession'))    

@app.route('/Create/Session', methods=['GET','POST'])
def createSession():
    if request.method == 'GET':
        return render_template('sessions/createSession.html')
    data = {
        'space' : Global.session['space'],
        'date' : request.form.get('date'),
        'cut' : request.form.get('cut'),
        'start' : request.form.get('start'),
        'end' : request.form.get('end')
    }
    SESSIONMODEL.createSession(data)
    return redirect(url_for('indexSession'))

@app.route('/Edit/Session/<idSession>', methods=['GET','POST'])
def editSession(idSession):
    if request.method == 'GET':
        return render_template('sessions/editSession.html', session = SESSIONMODEL.findSession(idSession))
    data = {
        'id': idSession,
        'space' : Global.session['space'],
        'date' : request.form.get('date'),
        'cut' : request.form.get('cut'),
        'start' : request.form.get('start'),
        'end' : request.form.get('end')
    }
    SESSIONMODEL.editSession(data)
    return redirect(url_for('indexSession'))

@app.route('/Remove/Session/<idSession>')
def removeSession(idSession):
    SESSIONMODEL.removeSession(idSession)
    return redirect(url_for('indexSession'))

