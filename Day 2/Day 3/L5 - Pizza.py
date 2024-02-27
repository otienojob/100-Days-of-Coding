# Pizza Order Module
visual = 2
p_price = 0
p_store = ["S", "M", "L"]

print(visual ** 10 * '-')
print("Welcome to the Python Pizza Deliveries\n\n")
print(visual ** 10 * '-')
print("Base price set to 0")
req_inp = input(print("Do we proceed to take your order? "))
if req_inp.upper() == "Y":
    p_size = input(print(f'What Pizza Size Would You Like to Order - {p_store}'))
    if p_size.upper() == "S":
        p_price += 15
        print("Current Bill: $", p_price)
    elif p_size.upper() == "M":
        p_price += 20
        print("Current Bill: $", p_price)
    else:
        p_price += 25
        print("Current Bill: $", p_price)
    print(visual ** 10 * '-')
    add_pepperoni = input(print('Would you like some extra pepperoni? "Y" for "Yes" and "N" for "No"'))
    if add_pepperoni.upper() == "Y":
        pep_size = input(print(f'Add for what size: {p_store}? '))
        if pep_size.upper() == "S":
            p_price += 2
            print(f'Unit price with pepperoni added is {p_price}')
        else:
            p_price += 3
            print(f'Unit price with pepperoni added is {p_price}')

    print(visual ** 10 * '-')
    add_cheese = input(print('Would you like some extra cheese? "Y" for "Yes" and "N" for "No"'))
    if add_cheese.upper() == 'Y':
        p_price += 1
        print("Your Bill is ", p_price)
        print(visual ** 10 * '-')

    else:
        print("Your Bill is ", p_price)


else:
    print("Look through our menu")
