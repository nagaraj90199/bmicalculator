import sys

weight = 60.0
height = 1.7

if len(sys.argv) == 3:
    weight = float(sys.argv[1])
    height = float(sys.argv[2])
else:
    print("No input given — using default values (60 kg, 1.7 m)")

bmi = weight / (height * height)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal weight"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print(f"BMI: {bmi:.2f} → {status}")
