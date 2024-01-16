print("Welcome the Tip Calculator!")
total = float(input("What is your total?\n"))
people = int(input("How many people split the bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))

total_per_person = total / people
tip_per_person = (tip*total_per_person)/100
amount = total_per_person+tip_per_person

print("The total amount you have to pay is: ")
print(amount)




