from flask import Flask, render_template, request, flash, session
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'faefagrafe324fafewaga'


menu = [{"name" : 'Send a message', "url": "/"}, 
        {"name" : 'Messages', "url": "/messages"}]


@app.route('/', methods=["POST", "GET"])
def hello():
    if request.method == 'POST':
        res = requests.post('http://backend:5002/addMessage', data={'message': f"{request.form['message']}"})
        if res.ok:
            flash('success', category="success")
        else:
            flash('error', category="error")
    return render_template('sendMessage.html', menu=menu)


@app.route('/messages', methods=["POST", "GET"])
def messages():
    if request.method == 'GET':
        res = requests.get('http://backend:5002/getMessages')
    return render_template('myMessages.html', title='Messages', menu=menu, messages=res.json() if res.ok else [('Error', 'Error')])

if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=False)
