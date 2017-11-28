from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def count():
 
    # read the posted values from the UI
    _input1 = request.form['workclass']
 
    # validate the received values
    return "output : " + _input1

if __name__ == "__main__":
    app.run()