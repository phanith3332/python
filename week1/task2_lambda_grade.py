# task2_lambda_grade.py

# Lambda function to check pass or fail
grade = lambda marks: "Pass" if marks >= 40 else "Fail"
# List of 6 marks
marks_list = [85, 72, 39, 45, 30, 60]
# Test each mark
for marks in marks_list:
    print("Marks:", marks, "->", grade(marks))

'''output:
Marks: 85 -> Pass
Marks: 72 -> Pass
Marks: 39 -> Fail
Marks: 45 -> Pass
Marks: 30 -> Fail
Marks: 60 -> Pass'''
