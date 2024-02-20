#This is a Band Name Generator Code

#variable declarations
city_name:str
pet_name:str
query:str

print("Welcome to Your Day One")
city_name=input(print("What is the name of the city you grew up in? "))
query=input(print("Do you have or have ever had a pet? Enter Y for Yes or N for No: "))
if query.upper()=="Y":
    pet_name=input(print("Enter the name of the pet"))
    print("And the suggested Band Name is: "+ city_name + " " + pet_name)
else:
    print("Better Luck")


    #end of code