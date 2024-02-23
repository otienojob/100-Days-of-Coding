#Pizza Order Module
visual=2
p_size:str
print(visual**5 * '-')
print("Welcome to the Python Pizza Palace\n\n")
req_inp=input(print("Do we proceed to take your order? "))
if req_inp.upper()=="Y":
    p_size=input(print('What Pizza Size Would You Like - "S", "M", or "L" ?'))
else:
    print("Look through our menu")