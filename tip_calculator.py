print("Helllooooo! Use the following program to calculate tip sharing!\n")

total_bill = float(input("What is the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))

tip = percentage_tip / 100 * total_bill
total_bill_plus_tip = total_bill + tip
tip_per_person = round((total_bill_plus_tip / number_of_people), 2)

print(f"\nEach person should pay ${tip_per_person}")