student_scores = input("Enter the student scores: ").split()
ans = int(student_scores[0])
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
    if student_scores[i] > ans:
        ans = student_scores[i]
print(f"The highest score in the class is: {ans}")
