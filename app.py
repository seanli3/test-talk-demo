from flask import Flask, jsonify, request, render_template
from bmi import calculateBmi
from persistence import add_bmi, get_bmi_list
from lifeML import get_life_expectancy

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/bmi", methods=['GET'])
def get_bmi():
    weight=request.args.get('weight', type=float)
    height=request.args.get('height', type=float)
    try:
        bmi = calculateBmi(weight, height)
        add_bmi(bmi)
        return jsonify(bmi=bmi)
    except ValueError as e:
        return str(e), 400


@app.route("/api/bmis", methods=['GET'])
def get_bmis():
    return jsonify(get_bmi_list() or [])

@app.route("/api/life-expectancy", methods=['GET'])
def get_age():
    return jsonify(age=get_life_expectancy())

if __name__ == '__main__':
    app.run(threaded=True)

