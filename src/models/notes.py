from src.config.db import DB
class notesModel():
    def listNotesStudents(self, idActivity):
        cursor = DB.cursor()
        cursor.execute(""" 
            SELECT 
            students.id,
            students.identification,
            students.name,
            students.surname,
            students.phone_number,
            students.email,
            students.semester,
            students.period_id,
            student_notes.note,
            student_notes.commentary,
            student_notes.id
            FROM student_notes 
            INNER JOIN students ON students.id = student_notes.student_id
            WHERE student_notes.partial_activity_id = ?
        """,(idActivity,))
        arrNotesStudents = cursor.fetchall()
        cursor.close()
        return arrNotesStudents

    def createNote(self,data):
        cursor = DB.cursor()
        cursor.execute('INSERT INTO student_notes(partial_activity_id, student_id,note,commentary) VALUES (?,?,?,?)',
        (data['activity'], data['student'], data['note'], data['commentary']))
        cursor.close()
    
    def findNote(self,idNote):
        cursor = DB.cursor()
        cursor.execute(""" 
            SELECT 
            students.identification,
            students.name,
            students.surname,
            students.semester,
            student_notes.note,
            student_notes.commentary
            FROM student_notes 
            INNER JOIN students ON students.id = student_notes.student_id
            WHERE student_notes.id = ?
        """,(idNote,))
        note = cursor.fetchone()
        cursor.close()
        return note

    def editNote(self,data):
        cursor = DB.cursor()
        cursor.execute(""" 
            UPDATE student_notes SET note = ?, commentary = ? WHERE id = ?
        """,(data['note'], data['commentary'], data['id']))
        cursor.close()
    
    def removeNote(self, idNote):
        cursor = DB.cursor()
        cursor.execute(""" DELETE FROM student_notes WHERE id = ? """,(idNote,))
        cursor.close()
