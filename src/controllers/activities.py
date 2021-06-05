from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.activitiesParcials import activitiesModel
from src.models.periods import periodsModel
from src.models.academicSpaces import academicModel
ACTIVITIESMODEL = activitiesModel()
ACADEMICMODEL = academicModel()
PERIODMODEL = periodsModel()

@app.route('/Activities/Parcials', methods=['GET','POST'])
@app.route('/Activities/Parcials/<space>', methods=['GET','POST'])
def indexActivities(space=None):
    if request.method == 'GET':
        if space != None:
            Global.session['space'] = space
        return render_template('activities_parcials/indexActivities.html', periods = PERIODMODEL.listPeriods(), 
        academicSpaces= ACADEMICMODEL.listAcademic(Global.session['period']), activities = ACTIVITIESMODEL.listActivities(Global.session['space']), pd = int(Global.session['space']))
    Global.session['space'] = request.form.get('space')
    return redirect(url_for('indexActivities'))

@app.route('/Create/Activities/Partials', methods=['GET','POST'])
def createActivitiesPartials():
    if request.method == 'GET':
        return render_template('activities_parcials/createActivities.html')
    data = {
        'name': request.form.get('name'),
        'date': request.form.get('date'),
        'cut': request.form.get('cut'),
        'porcentage': request.form.get('porcentage'),
        'academic_space' : Global.session['space']
    }
    ACTIVITIESMODEL.createActivity(data)
    return redirect(url_for('indexActivities'))

@app.route('/Edit/Activities/Partials/<idActivity>', methods=['GET','POST'])
def editActivitiesPartials(idActivity):
    if request.method == 'GET':
        return render_template('activities_parcials/editActivities.html', activity = ACTIVITIESMODEL.findActivity(idActivity))
    data = {
        'id': idActivity,
        'name': request.form.get('name'),
        'date': request.form.get('date'),
        'cut': request.form.get('cut'),
        'porcentage': request.form.get('porcentage'),
        'academic_space' : Global.session['space']
    }
    ACTIVITIESMODEL.editActivity(data)
    return redirect(url_for('indexActivities'))

@app.route('/Remove/Activities/Partials/<idActivity>')
def removeActivity(idActivity):
    ACTIVITIESMODEL.removeActivity(idActivity)
    return redirect(url_for('indexActivities'))