print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill? R"))
people_amount = float(input("How many people to split the bill? "))
tip_percentage = float(
    input("What percentage tip would you like to give? 10, 12, or 15? ")
)
amount_per_person = (
    (bill_amount * (tip_percentage / 100)) + bill_amount
) / people_amount
print(f"Each person should pay: R {str(round(amount_per_person,1))}")
