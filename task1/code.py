
# University Scholarship Allocation System

# Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

students = []

n = int(input("Enter number of students: "))

# Collect Student Details
for i in range(n):
    print("\nEnter details for Student", i + 1)

    name = input("Student Name: ")
    aggregate = float(input("Aggregate Marks: "))

    subjects = []
    num_subjects = int(input("Number of Subjects: "))

    for j in range(num_subjects):
        mark = float(input(f"Enter marks for Subject {j+1}: "))
        subjects.append(mark)

    attendance = float(input("Attendance Percentage: "))
    income = float(input("Annual Family Income: "))

    # Eligibility Checking
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARKS for mark in subjects) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        status = "Eligible"
    else:
        status = "Not Eligible"

    student = {
        "name": name,
        "aggregate": aggregate,
        "subjects": subjects,
        "attendance": attendance,
        "income": income,
        "status": status
    }

    students.append(student)


# Separate Eligible Students
eligible_students = [
    s for s in students if s["status"] == "Eligible"
]

# Ranking and Tie-Breaking Rules
eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        -sum(s["subjects"])
    )
)

# Display Eligible Students
print("\n===== SCHOLARSHIP ALLOCATION RESULT =====")

if eligible_students:
    print("\nEligible Students Ranked List:")

    for rank, student in enumerate(eligible_students, start=1):
        print("\nRank:", rank)
        print("Name:", student["name"])
        print("Aggregate Marks:", student["aggregate"])
        print("Attendance:", student["attendance"], "%")
        print("Family Income: Rs.", student["income"])
else:
    print("No eligible students found.")

# Display Not Eligible Students
print("\nNot Eligible Students:")

for student in students:
    if student["status"] == "Not Eligible":
        print(student["name"])

