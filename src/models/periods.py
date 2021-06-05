from src.config.db import DB
class periodsModel():
    def listPeriods(self):
        arrPeriods=[]
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM periods')
        for period in cursor:
            arrPeriods.append(period)
        cursor.close()
        return arrPeriods

    def createPeriod(self, data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO periods(date,period) VALUES(?,?)',(data['date'],data['period'],))
        cursor.close()

    def removePeriod(self,periodID):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM periods WHERE id = ?',(periodID,))
        cursor.close()

    def editPeriod(self, data):
        cursor = DB.cursor()
        cursor.execute("UPDATE periods SET date = ?, period = ? WHERE id = ?",(data['date'], data['period'], data['id'],))
        cursor.close()

    def findPeriod(self, idPeriod):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM periods WHERE id = ?',(idPeriod,))
        period = cursor.fetchone()
        cursor.close()
        return period
