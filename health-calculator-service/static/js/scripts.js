document.getElementById('bmi-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const weight = document.getElementById('weight').value;
  const height = document.getElementById('height').value;

  fetch('/bmi', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ weight: weight, height: height })
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('bmi-result').textContent = `BMI: ${data.bmi}`;
  });
});

document.getElementById('bmr-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const weight = document.getElementById('bmr-weight').value;
  const height = document.getElementById('bmr-height').value;
  const age = document.getElementById('age').value;
  const gender = document.getElementById('gender').value;

  fetch('/bmr', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ weight: weight, height: height, age: age, gender: gender })
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('bmr-result').textContent = `BMR: ${data.bmr}`;
  });
});