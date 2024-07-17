#Get the highest score from a list
print((2**5)* '--')
print("Instructions:")
print("1: Enter students' score separated by a space bar")
print("2: Press 'enter' to finish")
print((2**5)* '--')

class_scores=[]

class_score_input=input(print("Enter the score of students in a class: "))
class_scores=[name.strip() for name in class_score_input.split()]
print(class_scores)