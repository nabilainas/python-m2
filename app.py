from flask import Flask, request, jsonify

app = Flask(__name__)

# BMI Calculation
@app.route('/bmi', methods=['POST'])
def calculate_bmi():
  data = request.get_json()
  weight = data.get('weight')  # in kg
  height = data.get('height')  # in meters

  if not weight or not height:
    return jsonify({"error": "Weight and height are required"}), 400

  bmi = weight / (height ** 2)
  return jsonify({"bmi": round(bmi, 2)})

# BMR Calculation
@app.route('/bmr', methods=['POST'])
def calculate_bmr():
  data = request.get_json()
  weight = data.get('weight')  # in kg
  height = data.get('height')  # in cm
  age = data.get('age')  # in years
  gender = data.get('gender')  # male or female

  if not weight or not height or not age or not gender:
      return jsonify({"error": "Weight, height, age, and gender are required"}), 400

  if gender.lower() == 'male':
      bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
  elif gender.lower() == 'female':
      bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
  else:
      return jsonify({"error": "Invalid gender, must be 'male' or 'female'"}), 400

  return jsonify({"bmr": round(bmr, 2)})

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
