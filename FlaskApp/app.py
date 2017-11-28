from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/count',methods=['POST'])
def count():
 
    # read the posted values from the UI
    _input1 = request.form['input1']
    _input2 = request.form['input2']
    output = int(_input1) + int(_input2)
 
    # validate the received values
    return "output : " + str(output)

if __name__ == "__main__":
    app.run()