"""
You are going to write a program that calculates the average student height from a List of heights.

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Exemplo of input: 156 178 165 171 187
"""


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total_height = 0
number_of_students = 0

for i in student_heights:
    total_height += i
    number_of_students += 1

print(f"{round(total_height/number_of_students)}")
