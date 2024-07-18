#get sum of even numbers from 1 to x
print((2**5)* '--')
print("Instructions:")
print("'x' cannot be greater than '1000'")
print((2**5)* '--')

#error exception
user_input=0
while user_input<=0 or user_input>1000:
    try:
        user_input=int(input("Enter a value 'x'"))
        if user_input<=0 or user_input>1000:
            print("Invalid error. Enter a value between 1 and 1000")
    except ValueError:
        print("That's an invalid entry. Try again")
#end of exception block

sum_even=0
for n in range(2,user_input+1,2):
    sum_even+=n
    print(n,end=" ")

print(f'{sum_even}')