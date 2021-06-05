from src.config.db import DB
class assistanceModel():
    def listAssistance(self, idSession):
        cursor = DB.cursor()
        cursor.execute(""" 
            SELECT 
            c.date,
            c.cut,
            c.time_start,
            b.identification,
            b.name,
            b.surname,
            b.semester,
            a.assistance,
            a.id
            FROM session_student a
            INNER JOIN students b ON b.id = a.student_id
            INNER JOIN sessions c ON c.id = a.session_id
            WHERE a.session_id = ?
        """,(idSession,))
        arrAssistance = cursor.fetchall()
        cursor.close()
        return arrAssistance

    def createAssistance(self, data):
        cursor = DB.cursor()
        cursor.execute(""" INSERT INTO session_student(session_id,student_id,assistance) VALUES (?,?,?)""",
        (data['session'],data['student'],data['assistance'],))
        cursor.close()

    def findAssistance(self, idAssistance):
        cursor = DB.cursor()
        cursor.execute(""" 
            SELECT 
            b.identification,
            b.name,
            b.surname,
            b.semester,
            a.assistance
            FROM session_student a 
            INNER JOIN students b ON b.id = a.student_id
            WHERE a.id = ? 
        """,(idAssistance,))
        found = cursor.fetchone()
        cursor.close()
        return found

    def editAssistance(self, data):
        cursor = DB.cursor()
        cursor.execute(""" 
            UPDATE session_student SET assistance = ? WHERE id = ?
        """,(data['assistance'],data['id'],))
        cursor.close()
    
    def removeAssistance(self,assistance):
        cursor = DB.cursor()
        cursor.execute(""" DELETE FROM session_student WHERE id = ? """,(assistance,))
        cursor.close()