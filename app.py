from flask import Flask, request,render_template,redirect, url_for
app = Flask(__name__)
 
@app.route('/')
def hello(): 
    return 'Hello, World!'
 
@app.route('/form')
def hellohtml():
    return render_template("hello.html")
 
@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET':
         # args_dict = request.args.to_dict()
         #  # print(args_dict) 
        num = request.args["id"] 
        name = request.args.get("pw") 
        return "GET으로 전달된 데이터({}, {})".format(num, name) 
    else: 
        num = request.form["id"] 
        name = request.form["pw"]
        if num == "aaa" and name == "1234":
            return "({}, {})가 맞다".format(num, name)
        else:
            return "({}, {})가 아니다".format(num, name)
            
if __name__ == '__main__':
    app.run(debug=True)

