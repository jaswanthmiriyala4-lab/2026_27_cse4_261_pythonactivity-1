
# Hospital Billing and Patient Classification System

# Function to calculate hospital bill
def calculate_bill(consultation, diagnostic, treatment, age, card):

    total_bill = consultation + diagnostic + treatment

    concession = 0

    # Senior citizen concession
    if age >= 60:
        concession += 10

    # Concession card discount
    if card.lower() == "yes":
        concession += 5

    # Maximum concession limit
    if concession > 15:
        concession = 15

    discount_amount = total_bill * concession / 100

    final_bill = total_bill - discount_amount

    return total_bill, concession, discount_amount, final_bill


# Function to classify patient
def classify_patient(payment, final_bill):

    if payment == final_bill:
        return "Fully Paid"

    elif payment > 0:
        return "Partially Paid"

    else:
        return "Unpaid"


# Main Program
print("===== HOSPITAL BILLING SYSTEM =====")

# Patient Details
patient_id = input("Enter Patient ID: ")
name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))

# Billing Details
consultation = float(input("Enter Consultation Charges: Rs. "))
diagnostic = float(input("Enter Diagnostic Charges: Rs. "))
treatment = float(input("Enter Treatment Charges: Rs. "))

# Validate patient and billing details
if age < 0:
    print("Invalid age!")
    exit()

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid billing amount!")
    exit()

# Concession Card
card = input("Does patient have a concession card? (yes/no): ")

if card.lower() not in ["yes", "no"]:
    print("Invalid concession card input!")
    exit()

# Calculate Bill
total, concession, discount, final_bill = calculate_bill(
    consultation,
    diagnostic,
    treatment,
    age,
    card
)

# Payment Details
print("\nFinal Bill Amount: Rs.", round(final_bill, 2))

payment = float(input("Enter Amount Paid: Rs. "))

# Validate Payment
if payment < 0 or payment > final_bill:
    print("Invalid payment amount!")
    exit()

# Patient Classification
status = classify_patient(payment, final_bill)

# Calculate Balance
balance = final_bill - payment

# Display Final Bill
print("\n===== HOSPITAL BILL RECEIPT =====")

print("Patient ID:", patient_id)
print("Patient Name:", name)
print("Patient Age:", age)

print("\nConsultation Charges: Rs.", consultation)
print("Diagnostic Charges: Rs.", diagnostic)
print("Treatment Charges: Rs.", treatment)

print("\nTotal Bill: Rs.", round(total, 2))
print("Concession Applied:", concession, "%")
print("Discount Amount: Rs.", round(discount, 2))

print("Final Payable Amount: Rs.", round(final_bill, 2))
print("Amount Paid: Rs.", round(payment, 2))
print("Outstanding Balance: Rs.", round(balance, 2))

print("\nPatient Classification:", status)

print("\n===== BILLING COMPLETED =====")

