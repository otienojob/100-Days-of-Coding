#get the average height of students in a class

print((2**5)* '--')
print("Instructions:")
print("1: To enter multiple values, press spacebar for the next value")
print("2: Press enter to finish")
print((2**5)* '--')

class_height=[]

st_height_input=input(print("Enter the height of students in your class: "))
class_height=[name.strip() for name in st_height_input.split()]
print(class_height, " Values have been captured as String")
#convert list (string) to integer

new_class_height=[]
for x in class_height:
    new_class_height.append(int(x))
print("")
print("New Class List :", new_class_height)