#ticketing logic
ticket_price=0
u_name=input(print('Hello! Welcome to the "Ticketing Booth", What is your name?'))
height=int(input(print(f"\t{u_name}, please enter your height (cm) as a whole number!")))
if height > 120:
    user_age = int(input(print("\tKindly can you provide us with your age? ")))
    if user_age <= 12:
        ticket_price=5
        print(f'\tTicket Category: "Child" pricing for your age category {u_name} is ', ticket_price)
    elif user_age>12 and user_age<18:
        ticket_price=7
        print(f'\t\tTicket Category: "Youth" pricing for your age category {u_name} is ', ticket_price )
    else:
        ticket_price=12
        print(f'\t\tTicket Category: "Adult" cost for your age category{u_name} is', ticket_price)
    pic_request=str(input(print('Would you like a photo of your ride experience? Enter "Y" for "Yes" and "N" for "No" ')))
    if pic_request.upper()=="Y":
        new_ticket_price=ticket_price + 5
        print(f'You new ticket price {u_name} is $', new_ticket_price)
    else:
        print("Your ticket price remain unchanged ", ticket_price)

else:
    print("Sorry, you cannot go onto the ride")



print("End of Code")