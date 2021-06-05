from src.config.db import DB
class studentModel():
    def listStudents(self, idPeriod):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM students WHERE period_id = ?',(idPeriod,))
        arrStudents = cursor.fetchall()
        cursor.close()
        return arrStudents
    
    def findStudent(self, idStudent):
        cursor = DB.cursor()
        cursor.execute('SELECT * FROM students WHERE id = ?',(idStudent,))
        student = cursor.fetchone()
        cursor.close()
        return student
    
    def createStudent(self,data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO students(identification,name,surname,phone_number,email,semester,period_id) VALUES (?,?,?,?,?,?,?)',
        (data['identification'], data['name'], data['surname'], 
        data['phone_number'], data['email'], data['semester'],data['period_id'],))
        cursor.close()

    def removeStudent(self,idstudent):
        cursor = DB.cursor()
        cursor.execute('DELETE FROM students WHERE id = ?',(idstudent,))
        cursor.close()
    
    def editStudent(self,data):
        cursor = DB.cursor()
        cursor.execute('UPDATE students SET identification = ?, name = ?, surname = ?, phone_number = ?, email = ?, semester = ?, period_id = ? WHERE id = ?',
        (data['identification'],data['name'], data['surname'], data['phone_number'], data['email'], data['semester'], data['period_id'], data['id']))
        cursor.close()