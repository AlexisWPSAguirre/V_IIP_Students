from src.config.db import DB
class activitiesModel():
    def listActivities(self):
            cursor = DB.cursor()
            cursor.execute('SELECT * FROM partials_activities')
            arrActivities = cursor.fetchall()
            cursor.close()
            return arrActivities

    def createActivity(self, data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO partials_activities(academic_space_id,date,cut,name,porcentage_in_cut) VALUES(?,?,?,?,?)',
        (data['academic_space'], data['date'], data['cut'], data['name'], data['porcentage'],))
        cursor.close()
    
    def editActivity(self,data):
        cursor = DB.cursor()
        cursor.execute('UPDATE partials_activities SET academic_space_id = ?, date = ?, cut = ?, name = ?, porcentage_in_cut = ? WHERE id = ?',
        (data['academic_space'], data['date'], data['cut'], data['name'], data['porcentage'], data['id']))
        cursor.close()
    
    def findActivity(self,idActivity):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM partials_activities WHERE id = ?',(idActivity,))
        activity = cursor.fetchone()
        cursor.close()
        return activity
    
    def removeActivity(self,idActivity):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM partials_activities WHERE id = ?',(idActivity,))
        cursor.close()