bill = int(input("Please enter total bill amount: "))
level = input("Level of service (good/fair/bad): ")
people = int(input("Split how many ways?: "))

if level == "good":
    tip = (int(bill) * .2)

elif level == "fair":
    tip = (int(bill) * .15)

elif level == "bad":
    tip = (int(bill) * .1)

else:
    print("error")

print("Tip amount: $" + '%.2f' % float(tip))
print("Total amount: $ " + '%.2f' % float(bill + tip))
print("Amount per person: $" + '%.2f' % float((bill + tip) / people))