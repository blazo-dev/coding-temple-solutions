"""
👾 Final Challenge: Student Grade Program
🏆 Challenge: Write a program that takes a dictionary of students
👨‍🎓 and their grades, then prints
🖨️ each student's name and whether they passed
✅ or failed ❌ (consider passing as a grade ≥ 50).
"""

students = {
    'Alice': 85,
    'Bob': 42,
    'Charlie': 68,
    'David': 49
}

for student, grade in students.items():
    if grade >= 50:
        print(f"{student} passed.")
    else:
        print(f"{student} failed.")