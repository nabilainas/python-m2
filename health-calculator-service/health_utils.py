
def calculate_bmi(weight, height):
  
  if not weight or not height:
    return {"error": "Weight and height are required"}, 400

  bmi = weight / (height ** 2)
  return {"bmi": round(bmi, 2)}

def calculate_bmr(weight, height, age, gender):

  if not weight or not height or not age or not gender:
      return {"error": "Weight, height, age, and gender (male, female) are required"}, 400

  if gender.lower() == 'male':
      bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
  elif gender.lower() == 'female':
      bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
  else:
      return {"error": "Invalid gender, must be 'male' or 'female'"}, 400

  return {"bmr": round(bmr, 2)}
