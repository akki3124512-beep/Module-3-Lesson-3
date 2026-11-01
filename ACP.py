def bill(a, b):
    return a-b
total = int(input("Enter the total bill: "))
paid = int(input("Enter the amount ur paying: "))

if total==paid:
    print("You've paid enough.")
elif paid<total:
    print("You need to pay more.")
else:
    print("Your change is: ", bill(paid, total))