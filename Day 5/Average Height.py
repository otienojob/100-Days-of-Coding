#get the average height of students in a class

print((2**5)* '--')
print("Instructions:")
print("1: To enter multiple values, press spacebar for the next value")
print("2: Press enter to finish")
print((2**5)* '--')

class_height=[]

st_height_input=input(print("Enter the height of students in your class: "))
class_height=[name.strip() for name in st_height_input.split()]
print(f'{class_height}, Note: values have been captured as string.', end=' ')
print("Please convert values to integer!")
#convert list (string) to integer

new_class_height=[]
for x in class_height:
    new_class_height.append(int(x))
    # new_class_height=list(map(int, class_height))
print("")
print("New Class List :", new_class_height)
print((2**5)* '--')
print("Now, to calculate the average height of a student in a class")
sum_height=0
n_students=0
for n in new_class_height:
    #get the sum of height
    sum_height+=n
    n_students+=1

av_height=sum_height/n_students
round_av=round(av_height,2)
print(f' The Total Height Is: {sum_height}')
print(f' The Number of Students Is: {n_students}')
print(f' The Average Height Is: {round_av}')