print("Affinity Analyzer")
name1 = input("First Name\n")
name2 = input("Second Name\n")
combine = name1 + name2
final = combine.lower()

t = int(final.count("t"))
r = int(final.count("r"))
u = int(final.count("u"))
e = int(final.count("e"))
total1 = t + r + u + e

l = int(final.count("l"))
o = int(final.count("o"))
v = int(final.count("v"))
e = int(final.count("e"))
total2 = l + o + v + e

total = total1 + total2

print(f"your score is {total}")

if (total<10) or (total>90):
    print("you go together like coke and mentos")
elif (total>=40) and (total<=50):
    print ("well that's good")
else:
    print ("nothing to say")
