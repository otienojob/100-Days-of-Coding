#Create an application that marks a spot on a map with an x

print((2*6)*'**')
#creating grids on the map
line1=["A1","B1","C1"]
line2=["A2","B2","C2"]
line3=["A3","B3","C3"]

map=[line1,line2,line3]
hide_x=input()

if hide_x=="A1":
    hide_x.lower()=="a1"
    map[0][0]="X"
elif hide_x=="A2":
    hide_x.lower()=="a1"
    map[0][1]="X"
if hide_x=="A3":
    hide_x.lower()=="a1"
    map[0][2]="X"

print(map)

