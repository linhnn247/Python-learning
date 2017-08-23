height = float(input('Your height is: (cm) '))
weight = float(input('Your weight is: (kg) '))

heightm = height/100
BMI = weight/(heightm ** 2)
if BMI < 16:
    print('''Your BMI is: {0} so You're Severely underweight'''.format(round(BMI,2)))
elif BMI < 18.5:
    print('''Your BMI is: {0} so You're Underweight'''.format(round(BMI,2)))
elif BMI < 25:
    print('''Your BMI is: {0} so You're Normal'''.format(round(BMI,2)))
elif BMI <= 30:
    print('''Your BMI is: {0} so You're Overweight'''.format(round(BMI,2)))
else:
    print('''Your BMI is: {0} so You're Obese'''.format(round(BMI,2)))
