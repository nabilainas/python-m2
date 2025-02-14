
def calculate_bmi(weight, height):
  
  if not weight or not height:
    return {"error": "Weight and height are required"}, 400

  bmi = int(weight) / (float(height) ** 2)
  return {"bmi": round(bmi, 2)}

def calculate_bmr(weight, height, age, gender):

  if not weight or not height or not age or not gender:
      return {"error": "Weight, height, age, and gender (male, female) are required"}, 400

  if gender.lower() == 'male':
      bmr = 88.362 + (13.397 * int(weight)) + (4.799 * float(height)) - (5.677 * int(age))
  elif gender.lower() == 'female':
      bmr = 447.593 + (9.247 * int(weight)) + (3.098 * float(height)) - (4.330 * int(age))
  else:
      return {"error": "Invalid gender, must be 'male' or 'female'"}, 400

  return {"bmr": round(bmr, 2)}
