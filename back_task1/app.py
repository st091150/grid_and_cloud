from flask import Flask, request, g
import sqlite3
import json
import os

app = Flask(__name__)

DATABASE = 'siteDB.db'
DEBUG = True
SECRET_KEY = 'mtddg$@af5@7!tbfg#vvz&d7t2j6fs3bn'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'DB.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    return conn


def create_db():
    db = connect_db()
    sql = '''CREATE TABLE IF NOT EXISTS Messages(
            text TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );'''
    db.cursor().execute(sql)
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/addMessage', methods=["POST"])
def addMessage():
    res = dbase.addMessage(request.form['message'])
    return '', res

@app.route('/getMessages', methods=["POST", "GET"])
def getMessages():
    res = dbase.getMessages()
    if res != None:
        return json.dumps(res), 200
    else:
        return None, 400


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()
        

dbase = None
@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)

create_db()

if __name__ == '__main__':
    app.run(use_reloader=False)
