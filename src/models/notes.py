from src.config.db import DB
class notesModel():
    def listNotesStudents(self):
        cursor = DB.cursor()
        cursor.execute(""" 
            SELECT 
            student_notes.id,
            students.identification,
            students.name,
            students.surname,
            students.semester,
            student_notes.note,
            student_notes.commentary,
            student_notes.partial_activity_id
            FROM student_notes 
            INNER JOIN students ON students.id = student_notes.student_id
            """)
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
            student_notes.id,
            students.identification,
            students.name,
            students.surname,
            students.semester,
            student_notes.note,
            student_notes.commentary
            student_notes.partial_activity_id
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
            UPDATE student_notes SET student_id = ?, partial_activity_id = ?,note = ?, commentary = ? WHERE id = ?
        """,(data['student_id'],data['activity_id'],data['note'], data['commentary'], data['id']))
        cursor.close()
    
    def removeNote(self, idNote):
        cursor = DB.cursor()
        cursor.execute(""" DELETE FROM student_notes WHERE id = ? """,(idNote,))
        cursor.close()
