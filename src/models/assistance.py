from src.config.db import DB
class assistanceModel():
    def listAssistance(self):
        cursor = DB.cursor()
        cursor.execute(""" 
            SELECT 
            a.id,
            c.date,
            c.cut,
            c.time_start,
            b.identification,
            b.name,
            b.surname,
            b.semester,
            a.assistance
            FROM session_student a
            INNER JOIN students b ON b.id = a.student_id
            INNER JOIN sessions c ON c.id = a.session_id
        """)
        arrAssistance = cursor.fetchall()
        cursor.close()
        return arrAssistance

    def createAssistance(self, data):
        cursor = DB.cursor()
        cursor.execute(""" INSERT INTO session_student(session_id,student_id,assistance) VALUES (?,?,?)""",
        (data['session'],data['student'],data['assistance'],))
        cursor.close()

    def editAssistance(self, data):
        cursor = DB.cursor()
        cursor.execute(""" 
            UPDATE session_student SET student_id = ?, session_id = ?, assistance = ? WHERE id = ?
        """,(data['student'], data['session'], data['assistance'],data['id'],))
        cursor.close()
    
    def removeAssistance(self,assistance):
        cursor = DB.cursor()
        cursor.execute(""" DELETE FROM session_student WHERE id = ? """,(assistance,))
        cursor.close()