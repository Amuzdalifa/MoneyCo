from flask import Flask, render_template, request, jsonify
import json
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import maxabs_scale
from sklearn.externals import joblib

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def count():
    # read the posted values from the UI
    _input = [None] * 14
    with open('CensusIncome.names.txt', 'r') as fname:
        sname = fname.read()
    names=np.array(sname[sname.find("age"):].split(".\n"))

    #Encode Data Workclass
    workclass = preprocessing.LabelEncoder()
    workclass.fit(np.array(names[1][names[1].find(":")+2:].split(", ")))
    #print(workclass.classes_)

	#Encode Data Education
    education = preprocessing.LabelEncoder()
    education.fit(np.array(names[3][names[3].find(":")+2:].split(", ")))
    #print(education.classes_)
    marital_status = preprocessing.LabelEncoder()
    marital_status.fit(np.array(names[5][names[5].find(":")+2:].split(", ")))
    #print(marital_status.classes_)
    occupation = preprocessing.LabelEncoder()
    occupation.fit(np.array(names[6][names[6].find(":")+2:].split(", ")))
    #print(occupation.classes_)
    relationship = preprocessing.LabelEncoder()
    relationship.fit(np.array(names[7][names[7].find(":")+2:].split(", ")))
    #print(relationship.classes_)
    race = preprocessing.LabelEncoder()
    race.fit(np.array(names[8][names[8].find(":")+2:].split(", ")))
    #print(race.classes_)

    sex = preprocessing.LabelEncoder()
    sex.fit(np.array(names[9][names[9].find(":")+2:].split(", ")))
    #print(sex.classes_)

    native_country = preprocessing.LabelEncoder()
    native_country.fit(np.array(names[13][names[13].find(":")+2:].split(", ")))
    #print(native_country.classes_)

    _input[0] = float(request.form['age'])
    _input[1] = request.form['workclass']
    _input[2] = float(request.form['fnlwgt'])
    _input[3] = request.form['education']
    _input[4] = float(request.form['education-num'])
    _input[5] = request.form['marital-status']
    _input[6] = request.form['occupation']
    _input[7] = request.form['relationship']
    _input[8] = request.form['race']
    _input[9] = request.form['sex']
    _input[10] = float(request.form['capital-gain'])
    _input[11] = float(request.form['capital-loss'])
    _input[12] = float(request.form['hours-per-week'])
    _input[13] = request.form['native-country']
    temp = []
    temp.append(workclass.transform([_input[1]])[0])
    _input[1] = float(temp[-1])
    temp.append(education.transform([_input[3]])[0])
    _input[3] = float(temp[-1])
    temp.append(marital_status.transform([_input[5]])[0])
    _input[5] = float(temp[-1])
    temp.append(occupation.transform([_input[6]])[0])
    _input[6] = float(temp[-1])
    temp.append(relationship.transform([_input[7]])[0])
    _input[7] = float(temp[-1])
    temp.append(race.transform([_input[8]])[0])
    _input[8] = float(temp[-1])
    temp.append(sex.transform([_input[9]])[0])
    _input[9] = float(temp[-1])
    temp.append(native_country.transform([_input[13]])[0])
    _input[13] = float(temp[-1])

    dummy = []
    dummy.append(_input)
    test = np.array(dummy)
    test = maxabs_scale(test, axis=0, copy=False)
    bestmodel = joblib.load('Best.model')
    prediction = bestmodel.predict(test)
    if prediction[0]==1:
        result=">50K"
    else:
        result="<=50K"
    return render_template('result.html', messages={'result': result})

if __name__ == "__main__":
    app.run()