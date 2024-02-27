#Love Calculator


x=2
print(x**8 * '/')
print("Welcome to Your Love Compatibility App")
print(x**8 * '/')

names.insert(0,(input(print("Enter Your Partner's First Name"))))
names.insert(1,(input(print("Enter Your Second Name"))))
print(names)

print(x**8 * '/')

s_names=str(names)

T=s_names.lower().count('t')
R=s_names.lower().count('r')
U=s_names.lower().count('u')
E=s_names.lower().count('e')

score1=T+R+U+E
print(f'The letters making up your name appear {score1} times in the word "TRUE"')

L=s_names.lower().count('l')
O=s_names.lower().count('o')
V=s_names.lower().count('v')
E1=s_names.lower().count('e')

score2=L+O+V+E1
print(f'The letters making up your name appear {score2} times in the word "LOVE"')

score3=str(score1) + str(score2)
score4=int(score3)

print(x**8 * '/')

print("You have a total score of, ", score4, " Therefore: \n")

if (score4<=10) or (score4>90):
    print("The two of you go together like mentos")
elif (score4>=40) and (score4<=50):
    print("You are alright together")
else:
    print("Better Look for ALTERNATIVES")

p
print(x**8 * '/')

#count occurances of letters in 'true' and 'love'
#t=names.count("s",)
#print(t)

