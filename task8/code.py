
# Manufacturing Cost and Profitability Analysis

print("===== MANUFACTURING COST ANALYSIS =====")

# Input product details
product_name = input("Enter Product Name: ")

quantity = int(input("Enter Production Quantity: "))

material_cost = float(
    input("Enter Material Cost per Unit: ")
)

labour_cost = float(
    input("Enter Labour Cost per Unit: ")
)

wastage_rate = float(
    input("Enter Wastage Percentage: ")
)

machine_cost = float(
    input("Enter Total Machine Operating Cost: ")
)

selling_price = float(
    input("Enter Selling Price per Unit: ")
)

profit_target = float(
    input("Enter Required Profit Target (%): ")
)

# Calculate material cost
total_material_cost = material_cost * quantity

# Calculate labour cost
total_labour_cost = labour_cost * quantity

# Calculate wastage cost
wastage_cost = total_material_cost * wastage_rate / 100

# Calculate total manufacturing cost
total_manufacturing_cost = (
    total_material_cost +
    total_labour_cost +
    wastage_cost +
    machine_cost
)

# Calculate cost per unit
cost_per_unit = total_manufacturing_cost / quantity

# Calculate total revenue
total_revenue = selling_price * quantity

# Calculate profit or loss
profit = total_revenue - total_manufacturing_cost

# Calculate profit percentage
profit_percentage = (
    profit / total_manufacturing_cost
) * 100

# Check profit target
if profit_percentage >= profit_target:
    result = "PROFIT TARGET ACHIEVED"
else:
    result = "PROFIT TARGET NOT ACHIEVED"

# Display manufacturing statement
print("\n========== MANUFACTURING REPORT ==========")

print("Product Name             :", product_name)
print("Production Quantity      :", quantity)

print("------------------------------------------")
print("Total Material Cost      : Rs.",
      round(total_material_cost, 2))

print("Total Labour Cost        : Rs.",
      round(total_labour_cost, 2))

print("Wastage Cost             : Rs.",
      round(wastage_cost, 2))

print("Machine Operating Cost   : Rs.",
      round(machine_cost, 2))

print("------------------------------------------")
print("Total Manufacturing Cost : Rs.",
      round(total_manufacturing_cost, 2))

print("Manufacturing Cost/Unit  : Rs.",
      round(cost_per_unit, 2))

print("------------------------------------------")
print("Selling Price per Unit   : Rs.",
      round(selling_price, 2))

print("Total Sales Revenue      : Rs.",
      round(total_revenue, 2))

print("------------------------------------------")

if profit >= 0:
    print("Total Profit             : Rs.",
          round(profit, 2))
else:
    print("Total Loss               : Rs.",
          round(abs(profit), 2))

print("Profit Percentage        :",
      round(profit_percentage, 2), "%")

print("Required Profit Target   :",
      profit_target, "%")

print("------------------------------------------")
print("Production Status        :", result)

print("==========================================")

