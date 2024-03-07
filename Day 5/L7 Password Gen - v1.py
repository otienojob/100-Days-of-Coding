#Help users generate a password
import random

upper_caps=['A','B,','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
lower_caps=['a','b,','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
comb_case=[upper_caps,lower_caps]
pass_holder=""


print((2**5)*'...' )
name_input=input(print('Enter Your Name: '))
case_gen_req=int(input(print(f'How many letters would you like to generate {name_input}? ')))
for x in range(0,case_gen_req):
    pass_holder+=random.randrange(upper_caps(0,25))
    print()
    
#    pass_holder.append(random.randrange(upper_caps(0,9)))

#    pass_holder.append()
    print(x," ",pass_holder)





