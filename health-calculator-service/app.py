from flask import Flask, request
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
  data = request.get_json()
  weight = data.get('weight')
  height = data.get('height')
  return calculate_bmi(weight, height)

@app.route('/bmr', methods=['POST'])
def bmr():
  data = request.get_json()
  weight = data.get('weight')
  height = data.get('height')
  age = data.get('age')
  gender = data.get('gender')
  return calculate_bmr(weight, height, age, gender)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
