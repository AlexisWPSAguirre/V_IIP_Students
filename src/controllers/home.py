from flask import render_template, request, redirect, url_for, flash
from src import app
import src.controllers.period as Global
from src.models.periods import periodsModel
PERIODMODEL = periodsModel()

@app.route("/")
def index():
    return render_template('index.html', periods=PERIODMODEL.listPeriods())

@app.route("/Create/Period", methods=['GET','POST'])
def createPeriod():
    if request.method == 'GET':
        return render_template('periods/CreatePeriod.html')
    data = {
        'date' : request.form.get('date'),
        'period' : request.form.get('period')
    }
    PERIODMODEL.createPeriod(data)
    return redirect(url_for('index'))

@app.route("/Edit/Period/<idPeriod>", methods=['GET','POST'])
def editPeriod(idPeriod):
    if request.method == 'GET':
        return render_template('periods/EditPeriod.html', period = PERIODMODEL.findPeriod(idPeriod))
    data = {
        'id' : idPeriod,
        'date' : request.form.get('date'),
        'period' : request.form.get('period')
    }
    PERIODMODEL.editPeriod(data)
    return redirect(url_for('index'))
    
@app.route('/Remove/Period/<idPeriod>')
def removePeriod(idPeriod):
    PERIODMODEL.removePeriod(idPeriod)
    return redirect(url_for('index'))












    
    








