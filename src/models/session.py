from src.config.db import DB
class sessionModel():
    def listSession(self):
        cursor = DB.cursor()
        cursor.execute(""" 
            SELECT * FROM sessions""")
        arrSessions = cursor.fetchall()
        cursor.close()
        return arrSessions
    
    def createSession(self,data):
        cursor = DB.cursor()
        cursor.execute("""
            INSERT INTO sessions(academic_space_id,date,cut,time_start,time_end) VALUES (?,?,?,?,?)
        """,(data['space'], data['date'], data['cut'], data['start'], data['end']))
        cursor.close()

    def findSession(self,idSession):
        cursor = DB.cursor()
        cursor.execute(""" 
            SELECT * FROM sessions WHERE id = ?
        """,(idSession,))
        session = cursor.fetchone()
        cursor.close()
        return session
    
    def editSession(self, data):
        cursor = DB.cursor()
        cursor.execute(""" 
            UPDATE sessions SET date = ?, cut = ?, time_start = ?, time_end = ? WHERE id = ?
        """,(data['date'],data['cut'],data['start'],data['end'],data['id'],))
        cursor.close()
    
    def removeSession(self, idSession):
        cursor = DB.cursor()
        cursor.execute("""DELETE FROM sessions WHERE id = ? """,(idSession,))
        cursor.close()