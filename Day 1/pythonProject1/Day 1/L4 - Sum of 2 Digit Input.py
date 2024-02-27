#get an input of a double digit
#get the sum of the digits

num_input:int
val_1:int
val_2:int
sum_val:int

num_input=input(print('Enter a "doubtle" digit value: '))
val_1=num_input[0]
val_2=num_input[-1]
sum_val=val_1+val_2
print('The sum of the two digits', val_1, " and ", val_2, "is ", sum_val)