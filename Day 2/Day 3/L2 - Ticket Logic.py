#ticketing logic
u_name=input(print('Hello! Welcome to the "Ticketing Booth", What is your name?'))
height=int(input(print(f"\t{u_name}, please enter your height (cm) as a whole number!")))
if height > 120:
    user_age = int(input(print("\tKindly can you provide us with your age? ")))
    if user_age <= 12:
        print(f"\tTicket pricing for your age category {u_name} is $5.00")
    elif user_age>12 and user_age<18:
        print(f"\t\tTicket pricing for your age category {u_name} is $7.00 ", )
    else:
        print(f'\t\tThe ticket cost for your age category{u_name} is $12.00 [full adult price')
else:
    print("Sorry, you cannot go onto the ride")



print("End of Code")