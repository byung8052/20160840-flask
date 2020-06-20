from flask import Flask, request, render_template 
app = Flask(__name__) 

@app.route('/') 
def hello(): 
    return 'Hello, World!' 
    
@app.route('/hello') 
def hellohtml(): return render_template("hello.html") 
@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET': 
        # args_dict = request.args.to_dict() 
        # # print(args_dict) 
        num = request.args["id"] 
        name = request.args.get("pw") 
        return "GET으로 전달된 데이터({}, {})".format(num, name) 
    else: 
        num = request.form["id"] 
        name = request.form["pw"]
        with open("static/save.txt","w", encoding='utf-8') as f: 
            f.write("%s,%s" % (num, name))
        return "POST로 전달된 데이터({}, {})".format(num, name) 
if __name__ == '__main__': 
    app.run(debug=True)        


