print("Order your Pizza")
bill = 0
size = (input("what size pizza do you prefer? S,N or L\n"))
pep = (input("Do you want pepproni? Y/N\n"))
cheese = (input("Do you want extra cheese? Y/N\n"))

if size=="S":
    bill = 10
    if pep == "Y":
        bill = bill + 3
    if cheese == "Y":
        bill = bill + 1

elif size=="N":
    bill = 20
    if pep == "Y":
        bill = bill + 3
    if cheese == "Y":
        bill = bill + 1

elif size=="L":
    bill = 30
    if pep == "Y":
        bill = bill + 3
    if cheese == "Y":
        bill = bill + 1

print (f"your total bill will be {bill} ")
