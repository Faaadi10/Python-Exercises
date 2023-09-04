#getting the scores from the user

student_scores = input("enter all the marks with space between each").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

#displaying the entered scores

for n in range(0, len(student_scores)):
    print("The scores are :")
    print(student_scores[n])

# to check highest score

highest = 0
for score in student_scores:
    if score > highest:
        highest = score

print(f"the highest score is : {highest}")
