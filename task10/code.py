
# Campus Event Financial Planning System

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input fixed costs
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transportation cost: "))

# Input variable costs
catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

# Input financial details
sponsorship = float(input("Enter sponsorship amount: "))
contribution = float(input("Enter participant contribution: "))
participants = int(input("Enter expected number of participants: "))

# Calculate costs
fixed_cost = venue + equipment + transport

variable_cost = catering + certificate

total_cost = fixed_cost + (variable_cost * participants)

# Calculate participant contributions
total_contribution = contribution * participants

# Calculate total available funds
total_funds = sponsorship + total_contribution

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - total_funds)

# Calculate break-even registration count
balance_per_participant = contribution - variable_cost

if balance_per_participant > 0:
    required = max(
        0,
        int((fixed_cost - sponsorship
             + balance_per_participant - 1)
            // balance_per_participant)
    )
else:
    required = None

# Display results
print("\n===== FINANCIAL REPORT =====")

print("Fixed Cost:", fixed_cost)
print("Variable Cost per Participant:", variable_cost)
print("Total Event Cost:", total_cost)
print("Total Participant Contributions:", total_contribution)
print("Sponsorship Amount:", sponsorship)
print("Total Available Funds:", total_funds)
print("Sponsorship Shortfall:", shortfall)

if required is not None:
    print("Minimum Registrations to Break Even:", required)

    if participants >= required:
        print("Status: Event is financially feasible.")
    else:
        print("Status: More registrations are required.")
else:
    print("Break-even is not possible with the current")
    print("participant contribution.")

print("================================")

