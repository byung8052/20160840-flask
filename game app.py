from flask import Flask, request,render_template,redirect,url_for,abort
app = Flask(__name__)

import json 
import game

@app.route('/')
def hello(): 
    return 'Hello, World!'
 
@app.route('/form')
def hellohtml():
    return render_template("hello.html")

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_char(name)
    return render_template('game.html',data=character)

@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f: 
        data = f.read() 
        character = json.loads(data)
        print(character["skill"])
    return "{0} 기술을 사용하여 쓰러트렸다".format(character["skill"][0])

@app.route("/input/<int:num>")
def input_num(num):
    if num == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f: 
            data = f.read() 
            character = json.loads(data)
            print(character["skill"])
        return "{0} 기술을 사용하여 쓰러트렸다".format(character["skill"][0])
    else:
        return "도망갔다"
if __name__ == '__main__': 
    app.run(debug=True)
