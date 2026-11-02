
# Employee Payroll and Deduction Analysis

# Input employee details
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")

basic = float(input("Enter Basic Pay: "))
overtime_hours = float(input("Enter Overtime Hours: "))
incentives = float(input("Enter Incentives: "))

# Calculate allowances
da = basic * 0.10
hra = basic * 0.20
other_allowance = basic * 0.05

# Calculate overtime pay
overtime_pay = overtime_hours * 200

# Calculate gross salary
total_allowances = da + hra + other_allowance

gross_salary = (
    basic + total_allowances +
    overtime_pay + incentives
)

# Calculate progressive income tax
if gross_salary <= 25000:
    tax = 0
elif gross_salary <= 50000:
    tax = (gross_salary - 25000) * 0.05
elif gross_salary <= 100000:
    tax = (25000 * 0.05) + (
        gross_salary - 50000
    ) * 0.10
else:
    tax = (25000 * 0.05) + (50000 * 0.10) + (
        gross_salary - 100000
    ) * 0.15

# Calculate provident fund
pf = basic * 0.12

# Calculate total deductions
total_deductions = tax + pf

# Calculate net salary
net_salary = gross_salary - total_deductions

# Display salary statement
print("\n========== SALARY STATEMENT ==========")
print("Employee ID       :", emp_id)
print("Employee Name     :", name)
print("--------------------------------------")
print("Basic Pay         : Rs.", round(basic, 2))
print("DA (10%)          : Rs.", round(da, 2))
print("HRA (20%)         : Rs.", round(hra, 2))
print("Other Allowance   : Rs.", round(other_allowance, 2))
print("Overtime Pay      : Rs.", round(overtime_pay, 2))
print("Incentives        : Rs.", round(incentives, 2))
print("--------------------------------------")
print("Gross Salary      : Rs.", round(gross_salary, 2))
print("--------------------------------------")
print("Income Tax        : Rs.", round(tax, 2))
print("PF (12%)          : Rs.", round(pf, 2))
print("Total Deductions  : Rs.", round(total_deductions, 2))
print("--------------------------------------")
print("Net Salary        : Rs.", round(net_salary, 2))
print("======================================")

