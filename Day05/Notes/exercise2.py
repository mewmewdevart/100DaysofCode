student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

result = 0
max_value = 0
length = 0

for i in student_scores:
    length += 1

for i in range(1, length):
    if (student_scores[i] > student_scores[max_value]):
        max_value = i

print(f"The highest score in the class is: {student_scores[max_value]}")
