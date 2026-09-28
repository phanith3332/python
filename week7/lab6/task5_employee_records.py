# task5_employee_records.py

from functools import reduce
employees = [
    {"name": "Ravi", "department": "IT", "salary": 40000},
    {"name": "Sita", "department": "HR", "salary": 35000},
    {"name": "Amit", "department": "IT", "salary": 45000},
    {"name": "Priya", "department": "Finance", "salary": 50000},
    {"name": "Kiran", "department": "IT", "salary": 30000}
]
# Select employees from IT department using filter()
it_employees = list(
    filter(lambda emp: emp["department"] == "IT", employees)
)
# Give selected employees a 10% salary hike using map()
# Create new dictionaries without changing the originals
hiked_employees = list(
    map(
        lambda emp: {
            "name": emp["name"],
            "department": emp["department"],
            "salary": emp["salary"] * 1.10
        },
        it_employees
    )
)
# Calculate total salary expenditure using reduce()
total_salary = reduce(
    lambda total, emp: total + emp["salary"],
    hiked_employees,
    0
)
# Display results
print("IT Employees after 10% salary hike:")
for emp in hiked_employees:
    print(emp)
print("\nTotal Salary Expenditure:", total_salary)
print("\nOriginal Employee Records:")
for emp in employees:
    print(emp)

'''output:
IT Employees after 10% salary hike:
{'name': 'Ravi', 'department': 'IT', 'salary': 44000.0}
{'name': 'Amit', 'department': 'IT', 'salary': 49500.00000000001}
{'name': 'Kiran', 'department': 'IT', 'salary': 33000.0}

Total Salary Expenditure: 126500.0

Original Employee Records:
{'name': 'Ravi', 'department': 'IT', 'salary': 40000}
{'name': 'Sita', 'department': 'HR', 'salary': 35000}
{'name': 'Amit', 'department': 'IT', 'salary': 45000}
{'name': 'Priya', 'department': 'Finance', 'salary': 50000}
{'name': 'Kiran', 'department': 'IT', 'salary': 30000}'''

