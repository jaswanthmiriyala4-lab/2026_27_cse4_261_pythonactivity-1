Employee Payroll and Deduction Analysis Using Python
1. Problem Statement
Write a Python program to calculate an employee's monthly salary based on basic pay, allowances, overtime, and incentives.

The program should:

Read employee details such as employee ID, name, and basic pay.

Calculate allowances, overtime pay, and incentives.

Calculate the gross salary.

Apply progressive deductions based on the gross salary.

Calculate the total deductions and net salary.

Generate a formatted salary statement displaying all earnings and deductions.

Formula:

G
r
o
s
s
 
S
a
l
a
r
y
=
B
a
s
i
c
 
P
a
y
+
A
l
l
o
w
a
n
c
e
s
+
O
v
e
r
t
i
m
e
+
I
n
c
e
n
t
i
v
e
s
Gross Salary=Basic Pay+Allowances+Overtime+Incentives
N
e
t
 
S
a
l
a
r
y
=
G
r
o
s
s
 
S
a
l
a
r
y
−
T
o
t
a
l
 
D
e
d
u
c
t
i
o
n
s
Net Salary=Gross Salary−Total Deductions
2. Algorithm
Start.

Read employee ID and employee name.

Read basic pay.

Calculate allowances:

DA = 10% of basic pay.

HRA = 20% of basic pay.

Other allowance = 5% of basic pay.

Read overtime hours and calculate overtime pay at ₹200 per hour.

Read incentives.

Calculate gross salary by adding basic pay, allowances, overtime pay, and incentives.

Calculate progressive deductions:

Income tax:

0% for salary up to ₹25,000.

5% for the portion between ₹25,000 and ₹50,000.

10% for the portion between ₹50,000 and ₹1,00,000.

15% for the portion above ₹1,00,000.

PF = 12% of basic pay.

Calculate total deductions.

Calculate net salary.

Display the formatted salary statement.

Stop.

flowchart TD
    A([Start]) --> B[/Enter Employee ID and Name/]
    B --> C[/Enter Basic Pay/]
    C --> D[/Enter Overtime Hours and Incentives/]
    D --> E[Calculate DA, HRA and Other Allowance]
    E --> F[Calculate Overtime Pay]
    F --> G[Calculate Gross Salary]
    G --> H{Gross Salary <= 25000?}
    H -->|Yes| I[Tax = 0]
    H -->|No| J{Gross Salary <= 50000?}
    J -->|Yes| K[Tax = 5% of amount above 25000]
    J -->|No| L{Gross Salary <= 100000?}
    L -->|Yes| M[Tax = 5% first slab + 10% next slab]
    L -->|No| N[Tax = 5% + 10% + 15% progressive slabs]
    I --> O[Calculate PF = 12% of Basic Pay]
    K --> O
    M --> O
    N --> O
    O --> P[Calculate Total Deductions]
    P --> Q[Calculate Net Salary]
    Q --> R[/Display Salary Statement/]
    R --> S([Stop])
Thus, the Python program successfully calculates the employee's gross salary, applies progressive income tax and provident fund deductions, and generates a formatted salary statement showing the employee's net salary.

For the given sample input:

Gross Salary = ₹44,500

Total Deductions = ₹4,575

Net
Salary
=
₹39,925
