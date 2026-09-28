# lab2_task3.py

def total_marks(*marks):
    """Return the total and average of any number of marks."""
    total = sum(marks)
    average = total / len(marks)
    return total, average
# Test with 3 marks
total, average = total_marks(80, 75, 90)
print("3 Marks:")
print("Total:", total)
print("Average:", average)
# Test with 5 marks
total, average = total_marks(80, 75, 90, 85, 95)
print("\n5 Marks:")
print("Total:", total)
print("Average:", average)
# Test with 1 mark
total, average = total_marks(88)
print("\n1 Mark:")
print("Total:", total)
print("Average:", average)

'''output:
3 Marks:
Total: 245
Average: 81.66666666666667

5 Marks:
Total: 425
Average: 85.0

1 Mark:
Total: 88
Average: 88.0'''
