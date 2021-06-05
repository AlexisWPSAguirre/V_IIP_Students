from src.config.db import DB
class academicModel():
    def listAcademic(self, period):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM academic_spaces WHERE period_id = ?',(period,))
        arrAcademic = cursor.fetchall()
        cursor.close()
        return arrAcademic
    
    def createAcademicSpace(self, data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO academic_spaces(period_id,name,semester) VALUES(?,?,?)',(data['period_id'], data['name'], data['semester'],))
        cursor.close()
    
    def findAcademicSpace(self, idAcademicSpace):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM academic_spaces WHERE id = ?',(idAcademicSpace,))
        space = cursor.fetchone()
        cursor.close()
        return space

    def editAcademicSpace(self, data):
        cursor = DB.cursor()
        cursor.execute("UPDATE academic_spaces SET period_id = ?, name = ?, semester = ? WHERE id = ?",(data['period_id'], data['name'], data['semester'],data['id'],))
        cursor.close()
    
    def removeAcademicSpace(self,idSpace):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM academic_spaces WHERE id = ?',(idSpace,))
        cursor.close()