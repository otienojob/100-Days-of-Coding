#Select a Random Name from a List. Selected Name Pays for Dinner
import random

print((2**6)*"..")
friends_input=str(input(print("Begin by Capturing Names of Friends at a Dinner (Separate Names by 'Pressing the Space Bar'): "
)))
friends_list=[name.strip() for name in friends_input.split()]
random_bill=random.randrange(0,4)
person_to_pay_bill=friends_list[random_bill]
print(person_to_pay_bill + " is going to buy the meal today!")

#print(pick_name_to_pay_bill)

