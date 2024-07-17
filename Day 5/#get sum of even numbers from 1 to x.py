#get sum of even numbers from 1 to x
print((2**5)* '--')
print("Instructions:")
print("'x' cannot be greater than '1000'")
print((2**5)* '--')

#error exception
user_input=0
while user_input<=0 and user_input>1000:
    try:
        user_input=int(input("Enter a value 'x'"))
        if user_input<=0 or user_input>1000:
            print("Invalid error. Enter a value between 1 and 1000")
    except ValueError:
        print("That's an invalid entry. Try again")
#end of exception block