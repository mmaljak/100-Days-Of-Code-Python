print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
number_of_people = int(input("How many people to split the bill? "))

percentage = int(tip_percentage) / 100
print("Percentage: ", percentage)

tip_plus_bill = float(total_bill) * (1 + percentage)
print("Bill with the tip: ", tip_plus_bill)

per_person_bill = round((tip_plus_bill / number_of_people), 2)
print("Per person bill: ", per_person_bill)
per_person_bill = f"{per_person_bill:.2f}"

message = print(f"Each person should pay: ${per_person_bill}")
