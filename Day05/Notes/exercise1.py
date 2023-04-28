student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

som = 0
length = 0
result = 0

for i in student_heights:
    som += i

for i in student_heights:
    length += 1

result = round(som/length)
print(result)
