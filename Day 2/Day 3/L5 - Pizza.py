#Pizza Order Module
visual=2
p_size:str
p_store=["S","M","L"]
print(visual**5 * '-')
print("Welcome to the Python Pizza Deliveries\n\n")
req_inp=input(print("Do we proceed to take your order? "))
if req_inp.upper()=="Y":
    p_size=input(print(f'What Pizza Size Would You Like - {p_store}'))
    if p_size.upper()=="S":
        p_price=15
        print("Current Bill: $",p_price)
    elif p_size.upper()=="M":
        p_price=20
        print("Current Bill: $",p_price)
    elif p_size.upper()=="L":
        p_price=25
        print("Current Bill: $",p_price)
    add_pepperoni=input(print('Would you like some extra pepperoni? "Y" for "Yes" and "N" for "No"' ))
    if add_pepperoni.upper=="Y":
        pep_size=input(print('Add for "S", "M", or "L"? '))
    if pep_size.upper == "S":
        p_price+=2
        print(p_price)
    else:
        p_price+=3
        print(p_price)

else:
    print("Look through our menu")