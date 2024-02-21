from flask import Flask
from flask import render_template,jsonify,redirect,request

app=Flask(__name__)

@app.route("/")
def index():
    name=request.form.get("name")
    age=request.form.get("age")
    data={
        "name":name,
        "age":age
    }
    return jsonify({"msg":"success","data":data})

if __name__=="__main__":
    app.run(debug=True)