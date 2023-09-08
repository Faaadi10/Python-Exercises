bill = input ("what was your total bill?\n")
b = float(bill)
people = input ("how many people to split the bill ?\n")
p = int(people)
tip = input ("how much tip would you like to give? 10%, 20%, 30%\n")
t1 = int (tip)
t = (t1/100)
total_tip = b*t
total_amount = b + total_tip
amount_per_person = total_amount / p
final_amount = round(amount_per_person,2)
print(f"each person should pay {final_amount} ")
