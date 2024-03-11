import json

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
        
    def addMessage(self, message):
            sql = f'''INSERT OR IGNORE INTO Messages(text) VALUES('{message}');'''
            try:
                self.__cur.execute(sql)    
            except:
                return 400
            else:
                self.__db.commit()
                return 200
        

    def getMessages(self):
        sql = f'''SELECT * FROM Messages;'''
        try:
            self.__cur.execute(sql)  
            res = self.__cur.fetchall()
        except:
            return None
        else:
            return res


