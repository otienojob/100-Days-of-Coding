#Create an application that marks a spot on a map with an x

print((2*6)*'**')
#creating grids on the map
line1=["A1","B1","C1"]
line2=["A2","B2","C2"]
line3=["A3","B3","C3"]

map=[line1,line2,line3]
hide_x=input()

print((2*6)*'**')
if hide_x=="A1":
    map[0][0]="X"
elif hide_x=="B1":
    map[0][1]="X"
elif hide_x=="C1":
    map[0][2]="X"
elif hide_x=="A2":
    map[1][0]="X"
elif hide_x=="B2":
    map[1][1]="X"
elif hide_x=="C2":
    map[1][2]="X"
elif hide_x=="A3":
    map[2][0]="X"
elif hide_x=="B3":
    map[2][1]="X"
elif hide_x == "C3":
    map[2][2]="X"

print((2*6)*'**')    

print(f"{line1}\n{line2}\n{line3}")

print((2*6)*'**')

