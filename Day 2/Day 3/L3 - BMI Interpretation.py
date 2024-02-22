 #BMI Interpreter

print(2**7 * '-')
print("Body Mass Index (BM) Interpreter Based on Weight & Height")
u_weight=float(input(print("Enter Your Weight in KGs, e.g. 72")))
u_height=float(input(print("Enter Your Height in Meters, e.g. 1.55")))
print(2**7 * '-')

print("Calculating Your BMI\n")
b_m_i=u_weight/u_height**2
print(f'Your BMI is {b_m_i}\n')
print(2**7 * '-')

print(f"The interpretation of your BMI based on the {b_m_i} value is\n")
if b_m_i < 18.5:
    print(f'Your BMI is {b_m_i}, you are underweight')
elif b_m_i < 25:
    print(f'Your BMI is {b_m_i}, you have a normal weight')
elif b_m_i<30:
    print(f'Your BMI is {b_m_i}, you are slightly overweight')
elif b_m_i<35:
    print(f'Your BMI is {b_m_i}, you are obese')
else:
    print(f'Your BMI is {b_m_i}, you are clinically obese')