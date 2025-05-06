#Write a Python program to calculate the average marks for 5 subjects. The program should prompt the user to input the marks for each subject. After receiving the input, it should compute the average marks and then determine the corresponding grade based on the following grading system
"""# Input marks for 5 subjects
marks = []
for i in range(5):
    subject_marks = float(input(f"subject {i + 1}: "))
    marks.append(subject_marks)

# Calculate average marks
average_marks = sum(marks) / len(marks)

# Display average marks
print(f"Average Marks: {average_marks:.2f}")

# Assign grade based on average marks




# Display the grade
print(f"Grade: {grade}")
"""#sum = 0
sum = 0
for i in range(1,6):
	a= float(input(f"subject {i}: "))
	sum = sum + a
	avg = sum/5
print("Average Marks: %.2f"%avg)
if(avg>= 90 and avg<= 100):
	print("Grade: A\n")
elif(avg>= 80 and avg<= 89):
	print("Grade: B\n")
elif(avg>= 70 and avg<= 79):
	print("Grade: C\n")
elif(avg>= 60 and avg<= 69):
	print("Grade: D\n")
else:
	print("Grade: F\n")
