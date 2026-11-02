
# Retail Billing with Multiple Discount Rules

# Category-specific tax rates
tax_rates = {
    "food": 5,
    "clothing": 12,
    "electronics": 18,
    "furniture": 18
}

# Discount threshold rules
def get_discount_rate(amount):
    if amount >= 10000:
        return 20
    elif amount >= 5000:
        return 15
    elif amount >= 2000:
        return 10
    else:
        return 0


# Maximum concession limit
MAX_DISCOUNT = 2000

# Input number of products
n = int(input("Enter number of products: "))

products = []
grand_subtotal = 0

# Read product details
for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input(
        "Enter category (food/clothing/electronics/furniture): "
    ).lower()

    price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))

    if category not in tax_rates:
        print("Invalid category. Product skipped.")
        continue

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity. Product skipped.")
        continue

    subtotal = price * quantity

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal
    })

    grand_subtotal += subtotal


# Determine discount percentage
discount_rate = get_discount_rate(grand_subtotal)

# Calculate total discount
calculated_discount = grand_subtotal * discount_rate / 100

# Apply maximum concession limit
total_discount = min(
    calculated_discount,
    MAX_DISCOUNT,
    grand_subtotal
)

# Calculate effective discount percentage
if grand_subtotal > 0:
    effective_discount_rate = (
        total_discount / grand_subtotal
    ) * 100
else:
    effective_discount_rate = 0

# Generate itemized invoice
total_tax = 0

print("\n")
print("=" * 75)
print("                         RETAIL INVOICE")
print("=" * 75)

print(
    f"{'Product':15} {'Category':14} {'Qty':5} "
    f"{'Price':9} {'Discount':10} {'Tax':9} {'Total':10}"
)

print("-" * 75)

for product in products:

    subtotal = product["subtotal"]

    # Distribute overall discount proportionally
    item_discount = (
        subtotal * effective_discount_rate / 100
    )

    # Calculate category-specific tax
    tax_rate = tax_rates[product["category"]]

    taxable_amount = subtotal - item_discount

    item_tax = taxable_amount * tax_rate / 100

    item_total = taxable_amount + item_tax

    total_tax += item_tax

    print(
        f"{product['name']:15} "
        f"{product['category']:14} "
        f"{product['quantity']:<5} "
        f"{product['price']:<9.2f} "
        f"{item_discount:<10.2f} "
        f"{item_tax:<9.2f} "
        f"{item_total:<10.2f}"
    )

# Calculate final bill
final_amount = grand_subtotal - total_discount + total_tax

print("-" * 75)

print(f"{'Gross Subtotal':30} : Rs. {grand_subtotal:.2f}")
print(f"{'Discount Rate':30} : {discount_rate}%")
print(f"{'Total Discount':30} : Rs. {total_discount:.2f}")
print(f"{'Maximum Concession':30} : Rs. {MAX_DISCOUNT:.2f}")
print(f"{'Total Tax':30} : Rs. {total_tax:.2f}")

print("=" * 75)
print(f"{'FINAL PAYABLE AMOUNT':30} : Rs. {final_amount:.2f}")
print("=" * 75)

print("              THANK YOU! VISIT AGAIN!")

