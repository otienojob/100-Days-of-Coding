#find if a number is an odd number or even number


print("Get to Know If an Input (Integer) Is an Odd or Even Number! \n \t")
num_input=int(input(print("Enter value to evaluate: ")))

#decision point
if num_input % 2 == 0:
    print(f"The {num_input} is an even number")

else:
    print(f'The {num_input} is an odd number ')

print("End of Code")