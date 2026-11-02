
# Multi-Plan Telecommunications Cost Optimization

# Mobile plan details
plans = [
    {
        "name": "Basic Plan",
        "cost": 199,
        "data": 2,
        "calls": 200,
        "sms": 100,
        "validity": 28
    },
    {
        "name": "Standard Plan",
        "cost": 399,
        "data": 5,
        "calls": 500,
        "sms": 200,
        "validity": 56
    },
    {
        "name": "Premium Plan",
        "cost": 599,
        "data": 10,
        "calls": 1000,
        "sms": 500,
        "validity": 84
    },
    {
        "name": "Unlimited Plan",
        "cost": 799,
        "data": 20,
        "calls": 1500,
        "sms": 1000,
        "validity": 84
    }
]

# Excess usage rates
DATA_RATE = 50
CALL_RATE = 0.50
SMS_RATE = 0.20

# Get user requirements
print("===== MOBILE PLAN OPTIMIZATION =====")

required_data = float(input("Enter required data (GB): "))
required_calls = int(input("Enter required call minutes: "))
required_sms = int(input("Enter required SMS count: "))
required_validity = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs.): "))

# Store eligible plans
eligible_plans = []

print("\n========== PLAN COMPARISON ==========")

# Evaluate each plan
for plan in plans:

    # Calculate excess usage
    extra_data = max(0, required_data - plan["data"])
    extra_calls = max(0, required_calls - plan["calls"])
    extra_sms = max(0, required_sms - plan["sms"])

    # Calculate excess charges
    data_charge = extra_data * DATA_RATE
    call_charge = extra_calls * CALL_RATE
    sms_charge = extra_sms * SMS_RATE

    excess_charges = (
        data_charge + call_charge + sms_charge
    )

    # Calculate total cost
    total_cost = plan["cost"] + excess_charges

    # Check eligibility
    eligible = (
        total_cost <= budget and
        plan["validity"] >= required_validity
    )

    print("\nPlan Name       :", plan["name"])
    print("Plan Cost       : Rs.", plan["cost"])
    print("Extra Data      :", extra_data, "GB")
    print("Extra Calls     :", extra_calls, "minutes")
    print("Extra SMS       :", extra_sms)
    print("Excess Charges  : Rs.", round(excess_charges, 2))
    print("Total Cost      : Rs.", round(total_cost, 2))
    print("Validity        :", plan["validity"], "days")
    print("Eligible        :", "Yes" if eligible else "No")

    # Add eligible plans
    if eligible:
        eligible_plans.append({
            "name": plan["name"],
            "cost": total_cost,
            "validity": plan["validity"],
            "excess": excess_charges
        })

# Find the most economical plan
print("\n========== FINAL RECOMMENDATION ==========")

if eligible_plans:

    best_plan = min(
        eligible_plans,
        key=lambda x: x["cost"]
    )

    print("Most Economical Plan :", best_plan["name"])
    print("Total Cost           : Rs.",
          round(best_plan["cost"], 2))
    print("Excess Charges       : Rs.",
          round(best_plan["excess"], 2))
    print("Validity             :",
          best_plan["validity"], "days")

else:
    print("No eligible mobile plan found.")
    print("Please increase your budget or")
    print("reduce your usage or validity requirement.")

print("==========================================")
