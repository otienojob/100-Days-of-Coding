#Treasure Island Code Buil
print((2**7)*'-')
print('''\n .d8888b.  .d8888b. 8888888888 
d88P  Y88bd88P  Y88b      d88P 
888    888888    888     d88P  
888    888888    888    d88P   
888    888888    888 88888888  
888    888888    888  d88P     
Y88b  d88PY88b  d88P d88P      
 "Y8888P"  "Y8888P" d88P \n''')
print((2**7)*'-')
print("Welcome to Treasure Island.", end='')
print(" Your mission is to find the treasure.") 
print((2**7)*'-')

print("Make wise choices! Your life depends on it!")
turn_1=str(input(print("You have arrived at a crossroad! Would you like to take a 'right' or 'left' turn? ")))
if turn_1.lower() == 'left':
    print("CONGRADULATIONS! On to the next level")
    print("You have arrived at a the murky River Awach!")
    swim_1=input(print("What do you want to do? Do you want to 'SWIM' or 'WAIT' "))
    if swim_1.lower() == 'wait':
        print("CONGRADULATIONS! ")
        print('You have UNLOCKED LEVEL 3!')
        print('You are face-to-face with THREE DOORS! Which door color do you want to turn into? ')
    else:
        print("Uh Oh! You are SWIMMING with the SHARKS!.")
        print("Game Over")
else:
    print("Uh Oh! You have fallen into a bottomless PIT.")
    print("GAME OVER!")    



    