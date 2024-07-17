#Get the highest score from a list
print((2**5)* '--')
print("Instructions:")
print("1: Enter students' score separated by a space bar")
print("2: Press 'enter' to finish")
print((2**5)* '--')

class_scores=[]
new_class_score=[]

class_score_input=input(print("Enter the score of students in a class: "))
class_scores=[name.strip() for name in class_score_input.split()]
#convert input of string to int
new_class_score=list(map(int,class_scores))
print(f'Student Scores: {new_class_score}')
print((2**5)* '--')
#getting the highest score from a list
max_score=0
for x in new_class_score:
    if x > max_score:
        max_score=x
print(f'The highest score in the class is:, {max_score}')