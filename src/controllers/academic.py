from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.academicSpaces import academicModel
from src.models.periods import periodsModel
ACADEMICMODEL = academicModel()
PERIODMODEL = periodsModel()
@app.route('/Academic/Space', methods=['GET','POST'])
def indexAcademicSpace():
    if request.method == 'GET':
        if not 'period' in Global.session:
            Global.session['period'] = 1
        return render_template('academicSpaces/indexAcademicSpaces.html', periods = PERIODMODEL.listPeriods(), academicSpaces= ACADEMICMODEL.listAcademic(Global.session['period']), pd = int(Global.session['period']) )
    Global.session['period'] = request.form.get('period')
    return redirect(url_for('indexAcademicSpace'))

@app.route('/Create/Academic/Space', methods=['GET','POST'])
def createAcademicSpace():
    if request.method == 'GET':
        return render_template('academicSpaces/createAcademicSpace.html')
    data = {
        'name' : request.form.get('name'),
        'semester' : request.form.get('semester'),
        'period_id': Global.session['period']
    }
    ACADEMICMODEL.createAcademicSpace(data)
    return redirect(url_for('indexAcademicSpace'))

@app.route('/Edit/Academic/Space/<idSpace>', methods=['GET','POST'])
def editAcademicSpace(idSpace):
    if request.method == 'GET':
        return render_template('academicSpaces/editAcademicSpace.html', space = ACADEMICMODEL.findAcademicSpace(idSpace))
    data = {
        'id' : idSpace,
        'name' : request.form.get('name'),
        'semester' : request.form.get('semester'),
        'period_id': Global.session['period']
    }
    ACADEMICMODEL.editAcademicSpace(data)
    return redirect(url_for('indexAcademicSpace'))

@app.route('/Remove/Academic/Space/<idSpace>')
def removeAcademicSpace(idSpace):
    ACADEMICMODEL.removeAcademicSpace(idSpace)
    return redirect(url_for('indexAcademicSpace'))