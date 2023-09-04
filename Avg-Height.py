#getting the heights from user and converting each of them into int

student_height = input("Enter all your heights with spaces in between").split()
for n in range (0, len(student_height)):
    student_height[n] = int(student_height[n])


#finding the sum of heights and number of students

total = 0
number = 0
for student_height in student_height:
    total = total + student_height
    number = number + 1
print(total)
print(number)


#finding the average

avg = total/number
print(avg)



