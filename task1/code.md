University Scholarship Allocation System Using Python
1. Problem Statement
Design and develop a University Scholarship Allocation System using Python to evaluate student applications based on academic performance, attendance, and family income.

The system should:

Accept student details such as name, aggregate marks, subject-wise marks, attendance percentage, and annual family income.

Check whether students satisfy the minimum eligibility criteria.

Verify minimum marks in each subject.

Check attendance and income requirements.

Identify eligible students and rank them based on aggregate marks.

Resolve ties using predefined rules.

Display the final ranked list of scholarship recipients.

Eligibility Criteria (Example):

Aggregate marks: At least 75%.

Minimum marks in each subject: 60%.

Attendance: At least 75%.

Annual family income: Not more than ₹2,50,000.

Tie-breaking rules:

Higher aggregate marks.

Higher attendance percentage.

Lower annual family income.

Higher total subject marks.

2. Algorithm
Start the program.

Define the scholarship eligibility criteria.

Read the number of student applicants.

For each student, input:

Student name

Aggregate marks

Subject-wise marks

Attendance percentage

Annual family income

Check whether the aggregate marks are at least 75%.

Check whether every subject mark is at least 60%.

Check whether attendance is at least 75%.

Check whether annual family income is at most ₹2,50,000.

If all conditions are satisfied, mark the student as eligible.

Otherwise, mark the student as not eligible.

Sort eligible students using the predefined ranking and tie-breaking rules.

Display the eligible students in ranked order.

Display students who are not eligible.

Stop.
... Mermaid flowchat ...

    A([Start]) --> B[/Enter Number of Students/]
    B --> C[/Enter Student Details/]
    C --> D[/Enter Aggregate Marks/]
    D --> E[/Enter Subject-wise Marks/]
    E --> F[/Enter Attendance and Income/]

    F --> G{Aggregate >= 75?}

    G -- No --> N[Not Eligible]
    G -- Yes --> H{All Subject Marks >= 60?}

    H -- No --> N
    H -- Yes --> I{Attendance >= 75?}

    I -- No --> N
    I -- Yes --> J{Income <= 250000?}

    J -- No --> N
    J -- Yes --> K[Mark as Eligible]

    K --> L{More Students?}
    N --> L

    L -- Yes --> C
    L -- No --> M[Collect Eligible Students]

    M --> O[Sort by Aggregate Marks]
    O --> P[Break Ties Using Attendance]
    P --> Q[Break Ties Using Lower Income]
    Q --> R[Break Remaining Ties Using Subject Marks]

    R --> S[/Display Ranked Scholarship List/]
    S --> T[/Display Not Eligible Students/]
    T --> U([End])
    ...
    8. Conclusion
The University Scholarship Allocation System successfully evaluates student applications based on academic marks, subject-wise minimum scores, attendance, and family income.

It automatically identifies eligible students, ranks them according to academic performance, and resolves ties using predefined criteria.

Advantages:

Reduces manual work.

Ensures transparent scholarship allocation.

Avoids errors in eligibility checking.

Provides fair and consistent ranking.

Saves time during the scholarship selection process.


