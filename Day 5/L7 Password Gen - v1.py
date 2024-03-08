#Help users generate a password
import random

upper_caps=['A','B,','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
lower_caps=['a','b,','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
symbs=['~','!','@','#','$','%','^','&','*','(',')','_','+','+']
numbrs=[1,2,3,4,5,6,7,8,9,0]
pass_holder=""
act_passwrd=""
fin_passwrd=[]


print((2**5)*'...' )
name_input=input(print('Enter Your Name: '))
case_gen_req=int(input(print(f'How many letters would you like to generate {name_input}? ')))

print((2**5)*'...' )
for x in range(0,case_gen_req):
    fin_passwrd.append(random.choice(upper_caps))
    

print((2**5)*'...' )
for x in range(0,case_gen_req):
    fin_passwrd.append(random.choice(lower_caps))
    print(fin_passwrd)


print((2**5)*'...' )
for x in range(0,case_gen_req):
    fin_passwrd.append(random.choice(symbs))
    print(fin_passwrd)

print((2**5)*'...' )
for x in range(0,case_gen_req):
    fin_passwrd.append(random.choice(numbrs))
    print(fin_passwrd)

random.shuffle(fin_passwrd)

print((2**5)*'...' )

for x in fin_passwrd:
    act_passwrd+=x
    print(x)
#    act_passwrd+=x

print(act_passwrd)
    
    

#for x in range(0,case_gen_req):
#    pass_holder.append(random.choice(lower_caps))
#    pass_hold_str=str(pass_hold_str)
   

#for x in range(0,case_gen_req):
#    pass_holder.append(random.choice(symbs))
#    pass_hold_str=str(pass_hold_str)
    

#for x in range(0,case_gen_req):
#    pass_holder.append(random.choice(numbrs))
#    pass_hold_str=str(pass_hold_str)
    

#random.shuffle(pass_holder)
#act_passwrd=pass_holder

#for x in range(len(act_passwrd)):
#    y_in=x
#print(act_passwrd)
#print(y_in)
#    pass_holder.append(random.randrange(upper_caps(0,9)))

#    pass_holder.append()
#    print(x," ",pass_holder)





