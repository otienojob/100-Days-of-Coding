#calculate amount to pay
#calculate amount to pay + tip

#capture table details
table_host=input(print("Welcome to the Manour Eatery! What's your name? \n"))
print(f"Mr./Ms. {table_host}, kindly settle at table 10 \n")

bill_amount=3000
tip_percent=15


bill_response=input(print(f'Are you ready to settle your bill {table_host} \n:'))

if bill_response.upper()== "Y":
    print("Your Bill is: ", bill_amount)
    bill_split_request=input(print(f"Would you like to split the bill Mr./Ms {table_host}? \n"))
    if bill_split_request.upper()== "Y":
        bill_split_store=input(print("How many people would you like to split the bill between? \n"))
        tip_request=input(print("And would you like to add a tip to the bill? \n"))
    else:
        tip_request = input(print("And would you like to add a tip to the bill? \n"))
        if tip_request.upper() == "Y":
            tip_store = input(print("Do you want to tip 10%, 15% or 20% \n"))
            tip_store_string = [float(tip_store)]
            tip_percent = tip_store_string[0] / 100
            tip_amount = tip_percent * bill_amount
            new_bill_amount = tip_amount + bill_amount
            print("Bill per person is: ", new_bill_amount)
        if tip_request.upper()== "Y":
            tip_store=input(print("Do you want to tip 10%, 15% or 20% \n"))
            tip_store_string=[float(tip_store)]
            tip_percent=tip_store_string[0]/100
            tip_amount=tip_percent * bill_amount
            new_bill_amount=tip_amount+bill_amount
            bill_per_person=(new_bill_amount/int(bill_split_store))
            print("Bill per person is: ",bill_per_person)


else:
    print("Let me know when you are ready")




