student_heights = input("Input a list of student's heights: ").split()
ans = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    ans += student_heights[n]
print(round(ans / len(student_heights)))
