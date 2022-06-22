from flask import Flask
from flask import request,redirect
from flask import render_template

import re
import json
import speech_recognition as sr

my_keys = {
                'add':['added','add','adding','addition'],
                'sub':['subtracted','sub','subtracting','subtraction'],
                'multiply':['multiplied','multiple','multiplying','multiplication'],
                'swap':['swapped','swap','swapping'],
                'division':['divided','divide','divinding','division'],
                'factorial':['fact','factorial',],
                'bubble':['bubble','bubbling','bub'],
                'selection':['selection','selected','selecting','select'],
                'quick': ['quick','quicker','quickest'],
                'insertion':['insertion','insert','inserting','inserted'],
                'sort':['sorted','sort','sorting']
    }
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    result ={
        "Found": False,
        "Key": None
    }

    transcript = ''

    if request.method == "POST":
        file = request.files['audio_data']

        if file.filename == "":
           return redirect(request.url)

        if file:
            print(file)
            try:
                recognizer = sr.Recognizer()
                audioFile = sr.AudioFile(file)
                with audioFile as source:
                    data = recognizer.record(source)
                transcript = recognizer.recognize_google(data, key=None)
                print(transcript)
                transcript = transcript.lower()
            except sr.RequestError:
                result['Value'] = "API not reachable"
                with open("key.json", "w") as outfile:
                    json.dump(result, outfile)
                print("find3")
                return find()
            except sr.UnknownValueError:
                result['Value'] = "No audio"
                with open("key.json", "w") as outfile:
                    json.dump(result, outfile)
                print("find4")
                return find()

            for my_keys_key,my_keys_values in my_keys.items():
                for check_key in my_keys_values:
                    if check_key in transcript:
                        result['Found'] = True
                        result['Key'] = my_keys_key
                        with open("key.json", "w") as outfile:
                            json.dump(result, outfile)
                        print("find1")
                        # return find()


            pattern = re.findall(r"\ba\S+ion\b",transcript)
            if bool(pattern) and pattern[0] in transcript:
                result['Found'] = True
                result['Key'] = 'add'

            else:
                pattern = re.findall(r"\bm\S+ion\b",transcript)
                if bool(pattern) and pattern[0] in transcript:
                    result['Found'] = True
                    result['Key'] = 'multiply'
                else:
                    pattern = re.findall(r"\bs\S+ing\b",transcript)
                    if bool(pattern) and pattern[0] in transcript:
                        result['Found'] = True
                        result['Key'] = 'swap'
                    else:
                        pattern = re.findall(r"\bs\S+ion\b",transcript)
                        if bool(pattern) and pattern[0] in transcript:
                            result['Found'] = True
                            result['Key'] = 'sub'
                        else:
                            pattern = re.findall(r"\bso\S+ing\b",transcript)
                            if bool(pattern) and pattern[0] in transcript:
                                result['Found'] = True
                                result['Key'] = 'sort'

                            else:
                                pattern = re.findall(r"\bv\S+ion\b",transcript)
                                if bool(pattern) and pattern[0] in transcript:
                                    result['Found'] = True
                                    result['Key'] = 'division'
                                else:
                                    pattern = re.findall(r"\bf\S+ial\b",transcript)
                                    if bool(pattern) and pattern[0] in transcript:
                                        result['Found'] = True
                                        result['Key'] = 'factorial'



            result['Value'] = transcript
            # if result['Found'] == True:
            with open("key.json", "w") as outfile:
                json.dump(result, outfile)
            print("find2")
            # return find()
            # print("nan")
            # return jsonify(result)
        return render_template('index.html',transcript = transcript, request="POST")

            # return render_template('index.html', words=transcript, request="POST")
        # return render_template('index.html',transcript=transcript, request="POST")
    else:
        return render_template("index.html",transcript=transcript,request="GET")


@app.route("/find", methods=['POST',"GET"])
def find():

    # with open('data.json','r') as code_data,open('key.json','r') as key_data:   # file comprehension

    # with open('key.json','r') as key_data:
        # dict_code = json.load(code_data)          # converts .json into dict()
    with open('key.json','r') as key_data:
        dict_key = json.load(key_data)
        value = None
        contents = []
        findkey = dict_key['Key']
        if 'Value' in dict_key.keys():
            value = dict_key['Value']
            print(dict_key['Value'])


        contents.append(value)
        if findkey in my_keys.keys():
            contents.clear()
            with open(f'{findkey}.txt','r') as f:
                contents = f.readlines()


    return render_template('log.html', b_lines=contents)
    # return jsonify(result)      # returns result but first converts dict() into .json


if __name__ == "__main__":
    app.run(debug=True)
