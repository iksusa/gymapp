import json
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def read_data():
    with open('2week.json', 'r') as f:
        return json.load(f)

data = read_data()  

@app.route('/api/schedule', methods=['GET'])
def get_schedule():
    return jsonify(data['classes'])

def index():
    return render_template('3week(index).html')

if __name__ == '__main__':
    app.run(debug=True)